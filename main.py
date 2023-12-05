# -*- coding: utf-8 -*-
# import subprocess
import traceback
import time
import sys
# import pyttsx3
# import requests
# import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import os
from urllib.parse import unquote

# :: WEB SERVER SETTING
from flask import Flask, render_template, jsonify, url_for, request, redirect, abort
from flask import session

# :: DB SETTING
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, text
import pymysql
from config import config_web, config_db, db_url, url_paths, url_error_pages
from utility.data_model import employee_joined_list, employee_commutation_management_tb, db_session
# import mysql   # pip install mysql 수행 시 error 발생되어 주석처리.
# import config  # config.py 에서 config/__init__.py 로 대체되었음.


# from selenium import webdriver
# from random import randint, random
# from mutagen.mp3 import MP3
# from gtts import gTTS
# from datetime import datetime
# from bs4 import BeautifulSoup as bs
# import random
# import win32api


# import ssl     #ssl 보안레이어 추가시 사용
app = Flask(__name__, static_url_path="/static")
# app = Flask(__name__, static_url_path="/static/")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql-root@localhost/travel_mate?charset=utf8'
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = 'many      random     byte'
# app.config.from_pyfile("config.py")  # python 패키지를 만들면 __init__.py 가 생성된다
# app.config.from_object(config)
# app.config.from_envvar('APP_CONFIG_FILE') # 이걸 쓰려면 환경 변수를 추가해야한다. 안그럼 RuntimeError 가 발생  추후에 SETTING


# :: SESSION SETTING
# random bytes 시크릿 키 비밀번호로 app.secret_key 변수에 저장, 잘 보관해라 이 비밀번호를, 함부로 배포해서는 않되니 방법을 모색할것.
app.secret_key = b'f1748cc247d4d2978cda20416015bd551a90561e44e79b2a003a48bd646c4570'

# :: 파일 업로드 위치 SETTING
app.config['UPLOAD_FOLDER'] = 'storage/'




def get_server_time_as(time_style):
    now = time
    localtime = now.localtime()
    if time_style == '%Y_%m_%d_%H_%M_%S':
        return str(now.strftime('%Y_%m_%d_%H_%M_%S').replace('_', " "))
    elif time_style == '1':
        return str(now.time())
    elif time_style == '2':
        return str(now.strftime('%Y_%m_%d_%H_%M_%S'))
    elif time_style == '3':
        return str(now.strftime('%Y-%m-%d %H:%M:%S'))
    elif time_style == '4':
        return str(now.strftime('%Y-%m-%d %H:%M'))
    elif time_style == '5':
        return str(localtime.tm_year)
    elif time_style == '6':
        return str(localtime.tm_mon)
    elif time_style == '7':
        return str(localtime.tm_mday)
    elif time_style == '8':
        return str(localtime.tm_hour)
    elif time_style == '9':
        return str(localtime.tm_min)
    elif time_style == '10':
        return str(localtime.tm_sec)
    elif time_style == '11':
        return str(localtime.tm_wday)
    elif time_style == '12':
        elapsed_days_from_jan_01 = str(localtime.tm_yday)
        return elapsed_days_from_jan_01


# :: SERVER LOGGING
print(f' :: SERVER STARTED AT         : {get_server_time_as('%Y_%m_%d_%H_%M_%S')}''')
time_s = time.time()












# :: 파일 확장자 유효성 확인 기능
def check_allowed_file_or_not(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'toml'} # :: 파일 업로드 가능 확장자 SETTING


# :: CONTROLLER SETTING S
'''
페이지 라우팅 테스트 페이지
'''
@app.route('/urls-routing-test')
def test_urls_routing():
    if (request.method == 'GET'):
        content = f'<html><form name="fm_request"›'
        for key, value in url_paths.items():
            content += f'<li><a href="{url_paths[str(key)]}">{url_paths[str(key)]}</a></li> '
        content += f'</form></html>'
        return content
    else:
        abort(401)
        # SERVER에서 엑세스 거부 하도록 SETTING @app.route SETTING이 GET 으로 되어 있어 abort(401)은 도달하지 않을 코드 같다.


'''
에러 페이지
'''


@app.route("/error")
def route20231111132812():
    return render_template("/errors/error_default.html")


# '''
# 개발자 페이지
# '''
# @app.route('/temp')
# def route2023111110308():
#     return render_template("/developer.html")


# '''
# 관리자 페이지
# '''
# @app.route('/admin')
# def route2023111110309():
#     return render_template("/admin/main.html")


# '''
# 고객 페이지
# '''
# @app.route('/home')
# def route2023111110310():
#     return render_template("/home/main.html")


'''
스타팅 페이지 
'''


@app.route('/')
def render_index():
    return redirect('/employee/login')


@app.route('/employee')
def route2023111110315():
    try:
        print(f" :: session['name']: {session['name']}  session['id']: {session['id']}   session['pw']: {session['pw']}")
    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
        pass
    if (request.method == 'GET'):
        if 'id' in session and session['id'] != '':
            # :: session 기간 내에 로그인 한 경우
            # 이렇게 처리하면 안될듯 싶다... 이전페이지에서 FORM 으로 ID를 받아오는 것이 더 나은 방법인가?
            return render_template('/employee/main.html')
        else:
            # :: session 기간 내에 로그인 하지 않은 경우
            return render_template('/employee/login.html')
    elif (request.method == 'POST'):
        if 'id' in session and session['id'] == request.form['id']:
            # :: session 기간 내에 로그인 한 경우
            return render_template('/employee/main.html')
        else:
            # :: session 기간 내에 로그인 하지 않은 경우
            return render_template('/employee/login.html')
    else:
        abort(401)


@app.route('/employee/login')
def route20231111162108():
    # :: session 기간 내에 로그인 했었는지 확인
    if 'id' in session and session['id'] != '':
        return redirect('/employee')
    else:
        return render_template('/employee/login.html')


@app.route('/employee/login_', methods=['POST'])
def route2023111110312():
    # print(f' :: 로그인 입력 데이터 validation 2차 확인 로직''')
    # if validate_user_input(request.form['username'],request.form['pw']):
    #     return log_the_user_in(request.form['username'])
    # else:
    #     error = 'Invalid username/password'
    #     return render_template('login.html', error=error)


    # :: DB에 아이디와 PW가 동시에 일치하는 레코드가 있는지 확인
    employees_joined = employee_joined_list.get_employee_joined(id=request.form['id'], pw=request.form['pw'])


    print(f" :: employees_joined.first(): {employees_joined.first()}")
    if employees_joined.first() != None:
        # :: 세션에 데이터 저장
        session['id'] = request.form['id']
        session['login_time'] = get_server_time_as('%Y_%m_%d_%H_%M_%S')
        for employee_joined in employees_joined:
            print(f' :: employee_joined.name: {employee_joined.name}  employee_joined.id: {employee_joined.id}   employee_joined.pw: {employee_joined.pw}')
            session['name'] = employee_joined.name
        return f'''
        <script>
            //alert("로그인 되었습니다")
            setTimeout(function() {{
                window.location.href='/employee'  
                // window.close(); 
            }}, 500);
        </script>
        '''
    else:
        return f'''
                <script>
                    alert("패스워드 또는 아이디가 틀렸습니다.")
                    //alert("로그인에 실패하였습니다.")
                    setTimeout(function() {{
                        window.location.href='/employee'  
                        // window.close(); 
                    }}, 500);
                </script>
                '''



'''
로그아웃 페이지
'''
@app.route('/employee/logout', methods=['POST'])
def route20231111164103():
    # :: 세션에서 id 제거
    session.pop('id', None)

    # :: 세션 내 모든 값 삭제
    # session.clear()

    return redirect('/employee/login')


'''
회원가입 페이지
'''

@app.route('/employee/join', methods=['GET', 'POST'])
def route2023111110313():
    return render_template("/employee/join.html")


'''
회원가입 처리 페이지 
'''

@app.route('/employee/join_', methods=['POST'])
def route2023111110314():
    # :: 회원가입 조건 확인
    # 회원가입을 하면서 비밀번호와 비밀번호 확인이 일치하지 않은 경우
    if request.form['pw'] != request.form['pw2']:
        return f'''
        <script>
            alert('비밀번호가 일치하지 않습니다. 비밀번호를 일치하게 입력해주세요.')
            setTimeout(function() {{
                window.location.href='{'/employee/join'}'
            }}, 0);
        </script>
        '''

    # 회원가입을 하면서 아이디를 이미가입된 아이디로 한경우
    conn = pymysql.connect(
        host=config_db['host'],
        user=config_db['user'],
        password=config_db['password'],
        database=config_db['database'],
        charset='utf8'
    )
    cursor = conn.cursor()
    cursor.execute(f"""select count(*) id from employee_joined_list where id= "{request.form['id']}";""")
    result_tuple = cursor.fetchall()
    # print(result_tuple)
    # print(result_tuple[0])
    # print(result_tuple[0][0])
    # print(result_tuple[0][0]==0)
    print(result_tuple[0][0] != 0)
    if result_tuple[0][0] != 0:
        return f'''
                <script>
                    alert('이미가입된 아이디입니다. 다른 아이디로 회원가입을 시도해주세요.')
                    setTimeout(function() {{
                        window.location.href='{'/employee/join'}'
                    }}, 0);
                </script>
                '''
    row = cursor.fetchone()  # 데이타 Fetch one 하여 출력, jsp 에서 resultSet 처럼 쓰는 것 같다.
    while row:
        print(f' :: ''row :  {row[0]}  : {row[1]}''')
        row = cursor.fetchone()
    cursor.close()
    conn.close()

    # 회원가입을 하면서 아이디를 공백으로 한경우
    if request.form['id'] == '':
        return f'''
        <script>
            alert('아이디를 공백으로 회원가입을 할 수 없습니다.')
            setTimeout(function() {{
                window.location.href='{'/employee/join'}'  
                // window.close(); 
            }}, 0);
        </script>
        '''
    # 회원가입을 하면서 패스워드를 공백으로 한경우
    if request.form['pw'] == '':
        return f'''
        <script>
            alert('패스워드를 공백으로 회원가입을 할 수 없습니다.')
            setTimeout(function() {{
                window.location.href='{'/employee/join'}'  
                // window.close(); 
            }}, 0);
        </script>
        '''

    # :: ORM 사용해서 DB에 저장
    print(f' :: ORM 사용해서 DB에 저장''')
    employee_joined_list.add_new_records(name=request.form['name'], pw=request.form['pw'], phone_no=request.form['phone_no'], address=request.form['address'], e_mail=request.form['e_mail'], age=request.form['id'], id=request.form['id'], date_joined=get_server_time_as('%Y_%m_%d_%H_%M_%S'), date_canceled="")

    # :: 회원가입
    return f'''
    <script>
        alert("회원가입 되었습니다")
        setTimeout(function() {{
            window.location.href='/employee'  
            // window.close(); 
        }}, 0);
    </script>
    '''


'''
출근 처리 페이지
'''
def validate_phone_number(value):
    return value

@app.route('/employee/go-to-office', methods=['POST'])
def route2023111110321():
    # :: 변수에 저장
    server_time = get_server_time_as('%Y_%m_%d_%H_%M_%S')
    HH = server_time.split(' ')[3]
    mm = server_time.split(' ')[4]
    ss = server_time.split(' ')[5]
    name = session['name']
    employees = db_session.query(employee_joined_list).filter_by(id=session['id'], name=session['name']).limit(10).all()
    print(len(employees))
    if (len(employees) == 1):
        for employee in employees:
            # print(employee.id)
            # print(employee.name)
            # print(employee.phone_no)
            print(validate_phone_number(employee.phone_no))
            # :: employee_commutation_management_tb에 저장
            employee_commutation_management_tb.add_db_record(id=session['id'], name=session['name'], phone_no=employee.phone_no, time_to_go_to_office=server_time, time_to_leave_office='-')
    return f'''
        <div>{name} 님 {HH}시 {mm}분 {ss}초 출근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='/employee'  
                // window.close(); 
            }}, 2000);
        </script>
    '''


'''
퇴근 처리 페이지
'''
url_paths['url202311110410'] = '/employee/leave-office'


@app.route(url_paths['url202311110410'], methods=['POST'])
def route202311110410():
    # :: 변수에 저장
    server_time = get_server_time_as('%Y_%m_%d_%H_%M_%S')
    HH = server_time.split(' ')[3]
    mm = server_time.split(' ')[4]
    ss = server_time.split(' ')[5]
    name = session['name']
    employees = db_session.query(employee_joined_list).filter_by(id=session['id'], name=session['name']).limit(10).all()
    print(len(employees))
    if (len(employees) == 1):
        for employee in employees:
            # print(employee.id)
            # print(employee.name)
            # print(employee.phone_no)
            print(validate_phone_number(employee.phone_no))
            # :: employee_commutation_management_tb에 저장
            employee_commutation_management_tb.add_db_record(id=session['id'], name=session['name'], phone_no=employee.phone_no, time_to_go_to_office='-', time_to_leave_office=server_time)

    return f'''
        <div>{name} 님 {HH}시 {mm}분 {ss}초 퇴근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='/employee'  
                // window.close(); 
            }}, 2000);
        </script>
    '''


'''
업무 FAQ 공유
'''
url_paths['url202311100027'] = '/employee/faq-board'


@app.route(url_paths['url202311100027'], methods=['POST'])
def route2023111110316():
    datas = {
        'id': session['id'],
        'login_time': session['login_time'],
        'name': session['name'],
    }
    return render_template('/employee/faq_board.j2', name=datas)


'''
업무파일 백업 공유
'''
@app.route('/employee/file-upload')
def route20231111203226():
    # :: session 기간 내에 로그인 한 경우
    if 'id' in session and session['id'] != '':
        return '''
            <!doctype html>
            <title>파일 공유</title>
            <h1>파일 공유</h1>
            <!-- __________________________________________________________________________________________________________________________________ :: 파일 공유 처리 s -->
            <form name='form-file-upload' action="/employee/file-upload_" method="post" enctype="multipart/form-data">
                <input  type="file" name="file" value="promised202311110318" id="link20231111185433">
                <button type="submit">파일 업로드</button>
            </form>
            <!-- __________________________________________________________________________________________________________________________________ :: 파일 공유 처리 e -->
            '''
    else:
        # :: session 기간 내에 로그인 하지 않은 경우
        return render_template('/employee/login.html')


'''
파일 업로드 처리 페이지
'''
# from werkzeug.utils import secure_filename
@app.route('/employee/file-upload_', methods=['GET', 'POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return f'''
            <!doctype html>
            <script>
            alert("요청하신 파일이 없어 업로드에 실패했습니다");
            window.location.href = "/employee";
            </script>
            '''
    file = request.files['file']
    if file.filename == '':
        return f'''
            <!doctype html>
            <script>
            alert("요청하신 파일명이 공백으로 업로드할 수 없습니다");
            window.location.href = "/employee";
            </script>
            '''
    if file and check_allowed_file_or_not(file.filename):
        print(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        # return redirect('/employee')
        return f'''
            <!doctype html>
            <script>
            alert("파일이 업로드 되었습니다.");
            window.location.href = "/employee";
            </script>
            '''
    return f'''
    <!doctype html>
    <script>
    alert("파일 업로드 중 예외적인 상황이 발생했습니다. 관리자에게 문의해주세요. ");
    window.location.href = "/employee";
    </script>
    '''


'''
업무자동화 파일 공유
'''


@app.route('/employee/file-download')
def route202311161941():
    if 'id' in session and session['id'] != '':
        # :: session 기간 내에 로그인 한 경우
        datas = {
            'id': session['id'],
            'login_time': session['login_time'],
            'name': session['name'],
        }
        return render_template('/employee/utility_download.html', name=datas, context='????')
    else:
        # :: session 기간 내에 로그인 하지 않은 경우
        return render_template('/employee/login.html')


# params = {
#     "param1": id,
#     "param2": password,
#     "param3": name
# }
# res = requests.post("http://127.0.0.1:9090/handle_post", data=json.dumps(params))


'''
이 페이지는 아직 정의하지 않았습니다
'''


@app.route('/test-native-query')
def test_native_query_and_render():
    # print(" __________________________________________________________________________________________________________________________________ :: native_query to dictionary s[명시적이기 때문에 베스트 같다]")
    # db = pymysql.connect(
    #     host        =config_db['host'],
    #     user        =config_db['user'],
    #     password    =config_db['password'],
    #     database    =config_db['database'],
    #     charset='utf8'
    #     cursorclass = pymysql.cursors.DictCursor # 딕셔너리로 받기위한 커서
    # )
    # cursor = db.cursor()
    # sql = """
    #     select * from request_tb rt
    # """
    # cursor.execute(sql)
    # result_dictionary = cursor.fetchall()
    # print(result_dictionary)
    # pause()
    # print(" __________________________________________________________________________________________________________________________________ :: native_query to dictionary e")

    # print(" __________________________________________________________________________________________________________________________________ :: NATIVE_QUERY UPDATE SETTING s")
    # # row        = None
    # # connection = None
    # db = pymysql.connect(
    #     host        =config_db['host'],
    #     user        =config_db['user'],
    #     password    =config_db['password'],
    #     database    =config_db['database'],
    #     charset='utf8'
    #     cursorclass = pymysql.cursors.DictCursor
    # )
    # cursor = db.cursor()
    # values_to_bind = [
    #     {'CUSTOMER_NAME': '_박_정_훈_11_', 'MASSAGE': '주문서변경요청','DATE_REQUESTED': str(get_time_as_style("0"))},
    # ]
    # sql ='''
    #     UPDATE REQUEST_TB
    #     SET CUSTOMER_NAME = %(CUSTOMER_NAME)s ,
    #         MASSAGE = %(MASSAGE)s ,
    #         DATE_REQUESTED = %(DATE_REQUESTED)s
    #     WHERE ID_REQUEST = 11
    #     ;
    # '''
    # cursor.executemany(sql, values_to_bind)
    # db.commit()
    # pause()
    # print(" __________________________________________________________________________________________________________________________________ :: NATIVE_QUERY UPDATE SETTING e")

    print(" __________________________________________________________________________________________________________________________________ :: ORM INSERT SETTING s")
    engine = create_engine(db_url)
    Base = declarative_base()

    class REQUEST_TB(Base):
        __tablename__ = "REQUEST_TB"
        ID_REQUEST = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
        CUSTOMER_NAME = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
        MASSAGE = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
        DATE_REQUESTED = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
        USE_YN = sqlalchemy.Column(sqlalchemy.VARCHAR(length=2))

    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    session.add(REQUEST_TB(CUSTOMER_NAME="_박_정_훈_y_", MASSAGE="주문서변경요청", DATE_REQUESTED=get_server_time_as('%Y_%m_%d_%H_%M_%S'), USE_YN="Y"))
    session.commit()
    session.close()
    print(" __________________________________________________________________________________________________________________________________ :: ORM INSERT SETTING e")

    return ''


'''
FAQ 공유 상세페이지
'''


@app.route('/get/board/<id>')
def getId(id):
    print(id)
    return str(id)


'''
이 페이지는 아직 정의하지 않았습니다
'''


@app.route('/test-singlepage-data-request-via-get-post-request', methods=['GET', 'POST'])
def test_singlepage_request():
    if (request.method == 'GET'):
        content = ''
        content += ''' 
            <form name="fm_request"›  
                <p><input type="text" name="CUSTOMER_NM" placeholder="요청자명"></p> 
                <p><textarea name="MSG_REQUSETED" placeholder="요청사항을 입력하세요"></textarea></p>
                <p><input type="submit" value="제출" onclick="fm_submit()" ></p> 
            </form>
            <script>
                var url_to_submit = "%s"
                function fm_submit(){   
                    window.document.fm_request.method="post"
                    window.document.fm_request.autocomplete="on"
                    window.document.fm_request.action=url_to_submit
                    window.document.fm_request.submit()
                }
            </script>  
            <script>
                setTimeout(function() {
                    // window.location.href=url_to_submit    // redirect 
                    window.close(); 
                }, 10000);
            </script> 
        ''' % ('/test-singlepage-data-request-via-get-post-request')
        return content
    elif (request.method == 'POST'):

        CUSTOMER_NM = request.form['CUSTOMER_NM']
        MSG_REQUSETED = request.form['MSG_REQUSETED']
        content = ''
        content += f'''
            <div>{CUSTOMER_NM}</div>  
            <div>{MSG_REQUSETED}</div> 
            <script>
                //post 방식을 get 방식처럼 나오도록 하는 SINGLEPAGE_ROUTING 방법,   print(request.method) 동작을 확인 할 수 없음. js 가 java 보다 먼저 작동되는 것처럼 보인다. 
                //window.location.href = "{url_for('test_singlepage_request', CUSTOMER_NM=CUSTOMER_NM, MSG_REQUSETED=MSG_REQUSETED)}";
            </script>                       
        '''

        return content
    else:

        return redirect(url_error_pages["default"])


'''
이 페이지는 아직 정의하지 않았습니다
'''


@app.route('/SINGLEPAGE_ROUTING1', methods=['GET', 'POST'])
def test_singlepage_request_1():
    if (request.method == 'GET'):
        content = ''
        content += ''' 
            <form name="fm_request"›  
                <p><input type="text" name="CUSTOMER_NM" placeholder="요청자명"></p> 
                <p><textarea name="MSG_REQUSETED" placeholder="요청사항을 입력하세요"></textarea></p>
                <p><input type="submit" value="제출" onclick="fm_submit()" ></p> 
            </form>
            <script>
                var url_to_submit = "%s"
                function fm_submit(){   
                    window.document.fm_request.method="post"
                    window.document.fm_request.autocomplete="on"
                    window.document.fm_request.action=url_to_submit
                    window.document.fm_request.submit()
                }
            </script>  
            <script>
                setTimeout(function() {
                    // window.location.href=url_to_submit    // redirect 
                    window.close(); 
                }, 10000);
            </script> 
        ''' % ('/SINGLEPAGE_ROUTING1')

        return content
    elif (request.method == 'POST'):

        CUSTOMER_NM = request.form['CUSTOMER_NM']
        MSG_REQUSETED = request.form['MSG_REQUSETED']
        content = ''
        content += f''' 
            <script>
                //alert("{url_for('test_singlepage_request_1', CUSTOMER_NM=CUSTOMER_NM, MSG_REQUSETED=MSG_REQUSETED)}")
                //post 방식을 get 방식처럼 나오도록 하는 SINGLEPAGE_ROUTING 방법,   print(request.method) 동작을 확인 할 수 없음. js 가 java 보다 먼저 작동되는 것처럼 보인다. 
                window.location.href = "{url_for('test_singlepage_request_1', CUSTOMER_NM=CUSTOMER_NM, MSG_REQUSETED=MSG_REQUSETED)}";
            </script>                       
        '''

        return content
    else:
        return redirect(url_error_pages["default"])


'''
이 페이지는 아직 정의하지 않았습니다
'''


@app.route('/test/test/test', methods=['GET'])
def testtesttest():
    if (request.method == 'GET'):
        return f''' 
        <html>
            <form name="fm_request"›  
                <p><input type="text" name="CUSTOMER_NM" placeholder="요청자명"></p> 
                <p><textarea name="MSG_REQUSETED" placeholder="요청사항을 입력하세요"></textarea></p>
                <p><input type="submit" value="제출" onclick=fm_submit()></p> 
            </form>
            <script>
                var url_to_submit = "{url_paths['url202311100036']}" 
                function fm_submit(){{
                     window.document.fm_request.method="POST"
                     window.document.fm_request.autocomplete="on"
                     window.document.fm_request.action=url_to_submit
                     window.document.fm_request.submit()
                }}
            </script>
            <script>
                setTimeout(function() {{
                    window.location.href=url_to_submit  // redirect 
                    // window.close(); 
                }}, 10000);
            </script>
        </html>
        '''
    else:
        return redirect(url_error_pages["default"])


@app.route('/test/<string:user_name>', methods=['GET'])
def get_email(user_name):
    params = {'name': user_name}
    row = app.database.execute(text("""SELECT * FROM users WHERE name = :name"""), params).fetchone()
    return jsonify({'email': row['email']})


def main():
    # app.config.from_object(config) # config.py 를 사용해서 SETTING
    app.config.from_envvar('APP_CONFIG_FILE') # 환경변수 APP_CONFIG_FILE 에 정의된 파일을 사용해서 SETTING

    # :: development mode
    app.run(host=config_web['host'],port=config_web['port'],debug=True) # 왜 인지는 모르겠으나 debug=True 하면 os.system($url) 꼴로 작성한 코드가 두번 실행이 되었다.

    # :: pruduction mode
    # app.run(host=config_web['host'], debug=False, port=config_web['port'])

    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    # ssl_context.load_cert_chain(certfile='newcert.pem', keyfile='newkey.pem', password='secret')
    # app.run(host="0.0.0.0", port=4443, ssl_context=ssl_context, debug=False)


def open_routing_test_automatically():
    # :: url 라우팅 테스트
    # os.system(f'explorer "http://{config_web["host"]}:{str(config_web["port"])}/urls-routing-test' ) # '/urls-routing-test' = '/urls-routing-test'
    # os.system(f'explorer "http://{config_web["host"]}:{str(config_web["port"])}/temp' ) # '/temp' = '/temp'   # 개발자 페이지
    os.system(f'explorer "http://{config_web["host"]}:{str(config_web["port"])}/')
    # os.system(f'explorer "http://{config_web["host"]}:{str(config_web["port"])}{ url_paths['url202311111422'] ) # 페이지
    # os.system(f'explorer "http://{config_web["host"]}:{str(config_web["port"])}{ url_paths['url202311100027'] ) # 템플릿 실험
    # os.system(f'explorer "http://'+web["host"]+':'+str(web["port"])+''+'/get/board/<id>'.replace("<id>",str(int(random.random()*100))))

    # :: urls routing map
    # 추후 코드내에서 추출하기 용이하도록 코드작성규칙을 세워 작성.




if __name__ == '__main__':
    open_routing_test_automatically()
    try:
        main()
    except Exception as e:
        print(f' :: SERVER 실행 중 예외가 발생했습니다.''')
        
        traceback.print_exc(file=sys.stdout)
        print(e)
        # :: 세션 내 모든 값 삭제
        # session.clear()
        print(f' :: 세션 내 모든 값을 삭제하였습니다.''')


# :: ending log
time_e = time.time()
print(f' :: SERVER DID SHUTDOWN AT        : {get_server_time_as("%Y_%m_%d_%H_%M_%S")}')
print(f' :: SERVER LIFE CYCLE SPAN        : {time_e - time_s}')




