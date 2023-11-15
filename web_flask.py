import subprocess

import sqlalchemy
from sqlalchemy.orm import declarative_base

from config import config_web, config_db, db_url, url_paths, url_error_pages
from models.models import employee_joined_list

print(" __________________________________________________________________________________________________________________________________  encoding ")
# -*- coding: utf-8 -*-
print(" __________________________________________________________________________________________________________________________________  modules ")
import traceback
import time
import sys
# import pyttsx3
import requests
import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
import os
from urllib.parse import unquote
from selenium import webdriver
# from random import randint, random
from mutagen.mp3 import MP3
from gtts import gTTS
from datetime import datetime
from bs4 import BeautifulSoup as bs
import random
import win32api

print(" __________________________________________________________________________________________________________________________________  constant")
AI_available_cmd_code_list = [
    # '0:fake AI 가용명령목록 조회',
    # '`:single mode',
    # '``:batch mode',
    '`:advanced batch mode',
    'jhppc1:jhppc1',
    'remotedesktop:remote desktop',
    # 'voice mode:voice mode',
    # 'voiceless mode:voiceless mode',
    '시간:시간',
    '미세먼지랭킹:',
    '종합날씨:',
    '미세먼지:[없네..]',
    '초미세먼지:',
    '공간:공간',
    '체감온도:체감온도',
    '가용명령개수:가용명령개수',
    '종합날씨정보:종합날씨정보',
    '식물조언:식물조언',
    '스케쥴 모드:스케쥴 모드',
    'cls():cls()',
    'taskkill(알송):_________',
    '_________:_________',
    '172.30.1.33:_________',
    'sd_s:shutdown',
    'sd_e:shutdown cancelation',
    'x:exit'
]
high_frequency_batch_cmd_routine_pattern_list = [
    # '',
    'ex) 111111:[미세먼지정보]',
    # '',
    ''
]
nbsp = ' '
print(" __________________________________________________________________________________________________________________________________  function")


def cls():
    os.system('cls')


def all_info():
    print(" __________________________________________________________________________________________________________________________________  현재 pc에 연결된 드라이브 출력 s")
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    print(drives)
    print(" __________________________________________________________________________________________________________________________________  현재 pc에 연결된 드라이브 출력 e")
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 위치 s")
    print(os.getcwd())
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 위치 e")
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일의 Modified/Created/Accessed 일자 s")
    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    lines = current_files.split("\n")
    for line in lines:
        try:
            print("Modified : " + time.ctime(os.path.getmtime(line)))
            print("Created : " + time.ctime(os.path.getctime(line)))
            print("Accessed : " + time.ctime(os.path.getatime(line)))
        except:
            pass
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일의 일자 s")
    print(" __________________________________________________________________________________________________________________________________  생성된지 7일 된 모든 확장자 파일 출력 s")
    os.system('forfiles /P "E:\PRJS_PRIVATE\prj_memo\private.bkup" /S /M *.* /D -7 /C "cmd /c @echo @path" ')
    print(" __________________________________________________________________________________________________________________________________  생성된지 7일 된 모든 확장자 파일 출력 e")
    # print(" __________________________________________________________________________________________________________________________________  생성된지 1일 된 zip 확장자의 백업 파일 삭제 s")
    # os.system('forfiles /P "E:\PRJS_PRIVATE\prj_memo\private.bkup" /S /M *.zip /D -1 /C "cmd /c del @file" ')  # 2003 년 이후 설치 된 PC !주의! forfiles의 옵션이 달라서 큰 사이드 이펙트 일으킬 수 있음.
    # print(" __________________________________________________________________________________________________________________________________  생성된지 1일 된 zip 확장자의 백업 파일 삭제 e")
    print(" __________________________________________________________________________________________________________________________________  cmd.exe 실행 결과 한번에 출력 s")
    tmp = subprocess.check_output('dir /b /s /o /ad', shell=True).decode('utf-8')  # 폴더만
    tmp = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    tmp = subprocess.check_output('dir /b /s /o /a', shell=True).decode('utf-8')  # 전부
    print(tmp)
    print(" __________________________________________________________________________________________________________________________________  cmd.exe 실행 결과 한번에 출력 e")
    # print(" __________________________________________________________________________________________________________________________________  cmd.exe 실행 결과 한줄씩 출력 [실패] s")
    # current_files = os.popen('dir /b /s /o /a').readlines()    # 전부
    # current_files = os.popen('dir /b /s /o /ad').readlines()   # 폴더만
    # current_files = os.popen('dir /b /s /o /a-d').readlines()  # 파일만
    # for tmp in current_files:
    #     print(tmp)
    # print(" __________________________________________________________________________________________________________________________________  cmd.exe 실행 결과 한줄씩 출력 [실패] e")
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일만 사이즈 출력 s")
    # current_files = os.popen('dir /b /s /o /a').readlines()    # 전부
    # current_files = os.popen('dir /b /s /o /ad').readlines()   # 폴더만
    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    lines = current_files.split("\n")
    for line in lines:
        try:
            tmp = round(os.path.getsize(line.strip()) / (1024.0 * 1024.0), 2)
            if (tmp < 1):
                print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0), 2)) + ' KB')
            elif (tmp < 1024):
                print(line.strip() + " : " + str(round(os.path.getsize(line.strip()) / (1024.0 * 1024.0), 2)) + ' MB')
            else:
                print(line.strip() + " : " + str(
                    round(os.path.getsize(line.strip()) / (1024.0 * 1024.0 * 1024.0), 2)) + ' GB')
        except:
            pass
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일만 사이즈 출력 e")
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일만 사이즈 출력2 s")

    def convert_size(size_by_tes):
        import math
        if size_by_tes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_by_tes, 1024)))
        p = math.pow(1024, i)
        s = round(size_by_tes / p, 2)
        return "%s %s" % (s, size_name[i])

    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    lines = current_files.split("\n")
    for line in lines:
        try:
            print(line.strip() + "{{delimeter}}" + str(convert_size(os.path.getsize(line.strip()))))
        except:
            pass
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일만 사이즈 출력2 e")
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일만 생성일자 출력 s")
    current_files = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8')  # 파일만
    lines = current_files.split("\n")
    for line in lines:
        try:
            # print(os.path.getmtime(line.strip()))
            # print(time.ctime(os.path.getmtime(line.strip())))
            # print(line.strip() + "{{delimeter}}" + str(os.path.getctime(line.strip())))
            # print(line.strip() + "{{delimeter}}" + str(datetime.datetime.fromtimestamp(os.path.getctime(line.strip())).strftime('%Y-%m-%d %H:%M:%S')))
            print(line.strip() + "{{delimeter}}" + str(time.ctime(os.path.getmtime(line.strip()))))
        except:
            pass
    print(" __________________________________________________________________________________________________________________________________  현재 디렉토리 파일만 생성일자 출력 e")
    print(" __________________________________________________________________________________________________________________________________  20230414 18:00 이후 생성된 파일 출력 s")
    inputDate = datetime.strptime(str(input('Searching Input Date : ')), '%Y%m%d %H:%M')
    opening_directory = r'D:\test'
    for (path, dir, files) in os.walk(opening_directory):
        for filename in files:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
            if inputDate < fileMtime:
                print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' % (path, filename, fileMtime))
    print(" __________________________________________________________________________________________________________________________________  20180526 14:00 이후 생성된 파일 출력 e")
    print(" __________________________________________________________________________________________________________________________________  20230414 18:00 이전 생성된 파일 출력 s")
    inputDate = datetime.strptime(str(input('Searching Input Date : ')), '%Y%m%d %H:%M')
    opening_directory = r'D:\test'
    for (path, dir, files) in os.walk(opening_directory):
        for filename in files:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
            if inputDate > fileMtime:
                print('경로 : [%s], 파일명 : [%s], 수정일자 : [%s]' % (path, filename, fileMtime))
                print('[%s\%s]' % (path, filename))
    print(" __________________________________________________________________________________________________________________________________  20180526 14:00 이전 생성된 파일 출력 e")
    print(" __________________________________________________________________________________________________________________________________  현재시간기준 생성된지 1일 된 zip 확장자 파일만 출력 s")
    times = get_time_as_style("0").split(' ')
    time_inputed = times[0] + times[1] + str(int(times[2]) - 1) + " " + times[3] + ":" + times[4]
    print(time_inputed)
    time_inputed = '20230414 20:53'
    print(time_inputed)
    inputDate = datetime.strptime(str(time_inputed), '%Y%m%d %H:%M')
    opening_directory = opening_directory
    for (path, dir, files) in os.walk(opening_directory):
        for filename in files:
            fileMtime = datetime.fromtimestamp(os.path.getmtime(path + '\\' + filename))
            if inputDate < fileMtime:
                print('[%s\%s    modified : %s]' % (path, filename, fileMtime))
                print('[%s\%s]' % (path, filename))
                print('[%s]' % (filename))
    pause()
    print(" __________________________________________________________________________________________________________________________________  현재시간기준 생성된지 1일 된 zip 확장자 파일만 출력 e")
    print(" __________________________________________________________________________________________________________________________________  __________.xls s")
    print(" __________________________________________________________________________________________________________________________________  __________.xls e")
    print(" __________________________________________________________________________________________________________________________________  __________.json writing s")
    import json
    data_dict = {
        'ID_REQUEST': 1,
        'CUSTOMER_NAME': '_박_정_훈_',
        'MASSAGE': '주문서변경요청',
        'DATE_REQUESTED': get_time_as_style("1"),
        'USE_YN': "Y",
    }
    data_str = json.dumps(data_dict, indent=4)
    print(data_str)

    data_dict = {}
    data_dict['head'] = []
    data_dict['head'].append({
        "title": "Android Q, Scoped Storage",
        "url": "https://codechacha.com/ko/android-q-scoped-storage/",
        "draft": "false"
    })
    data_dict['body'] = []
    data_dict['body'].append({
    })
    data_dict['config'] = []
    data_dict['config'].append({
        "host": config_web['host'],
        "port": config_web['port'],
    })
    print(data_dict)
    print(type(data_dict))
    json_file_path = "./json/__________.json"
    with open(json_file_path, 'w') as outfile:
        json.dump(data_dict, outfile, indent=4)
    print(" __________________________________________________________________________________________________________________________________  __________.json writing e")
    print(" __________________________________________________________________________________________________________________________________  __________.json JSON Encoding s")
    data_dict = {
        'ID_REQUEST': 1,
        'CUSTOMER_NAME': '_박_정_훈_',
        'MASSAGE': '주문서변경요청',
        'DATE_REQUESTED': get_time_as_style("1"),
        'USE_YN': "Y",
        'MARVEL CHARACTERS': [
            {'MACHANICAL MEMBER1': ['IRONMAN', 'BLACK PANTHER']},
            {'MITHICAL MEMBER1': ['ROKI', 'THOR PANTHER']},
        ]
    }
    print(data_dict)
    print(type(data_dict))
    json_file_path = "./json/__________.json"
    with open(json_file_path, 'w') as outfile:
        json.dump(data_dict, outfile, indent=4)
    print(" __________________________________________________________________________________________________________________________________  __________.json JSON Encoding e")
    print(" __________________________________________________________________________________________________________________________________  __________.json JSON Decoding s")
    # json 파일을 가져와서 python data type[Dictionary, List, Tuple , str] 으로 변환하는 작업
    data_str = '{"name": "강진수", "id": 152352, "history": [{"date": "2015-03-11", "item": "iPhone"}, {"date": "2016-02-23", "item": "Monitor"}]}'
    data_dict = json.loads(data_str)

    print(json.dumps(data_dict, indent=4, sort_keys=True))
    print(data_dict['name'])
    print(data_dict['id'])
    for depth_level1 in data_dict['history']:
        print(depth_level1['date'], depth_level1['item'])
    print(" __________________________________________________________________________________________________________________________________  __________.json JSON Decoding e")
    print(" __________________________________________________________________________________________________________________________________  __________.json e")
    print(" __________________________________________________________________________________________________________________________________  __________.yaml s")
    import yaml  # pip install PyYAML
    with open('__________.yaml') as f:
        conf = yaml.load(f)
    __________1 = conf['language']
    __________2 = conf['pytest']
    print(__________1)
    print(__________2)
    print(" __________________________________________________________________________________________________________________________________  __________.yaml e")
    print(" __________________________________________________________________________________________________________________________________  doctest s")
    import doctest
    def ipconfig():
        """
            _____________________________________________________________________ description s
            author      : jung hoon park
            c:\> ipconfig
                    └>This function works like
            c:\> python _________.py
                        └>we can try like this
            c:\> python _________.py -v
                        └>we can try like this, if you want to more info.
            _____________________________________________________________________ description e
            >>> ipconfig()
            ???
        """
        return os.system('ipconfig')

    doctest.testmod()
    print(" __________________________________________________________________________________________________________________________________  doctest e")
    print(" __________________________________________________________________________________________________________________________________  pytest s")

    print(" __________________________________________________________________________________________________________________________________  pytest e")
    print(" __________________________________________________________________________________________________________________________________  data test s")
    print("데이터의 흐름 변화 그 안에서 마주하게된 정렬에 대한 필요성")
    data = __________1

    def checkData(__________):
        """
            _____________________________________________________________________ checkData(__________) doc s
            author      : jung hoon park
            c:\> ipconfig
                    └>This function works like this
            c:\> python _________.py
                        └>we can try like this
            c:\> python _________.py -v
                        └>we can try like this, if you want to more info.
            _____________________________________________________________________ checkData(__________) doc e
            >>> ipconfig()
            ???
        """
        if type(__________) == 'None':
            print(None)
        if type(__________) == 'String':
            print('String')
        if type(__________) == 'String':
            print('String')
        elif type(__________) == None:
            print(None)

    print(" __________________________________________________________________________________________________________________________________  data test e")
    print(" __________________________________________________________________________________________________________________________________  f-sting python 문자열 포매팅 s")  # f-sting 은 파이썬 3.6 이후 기능
    number = 3
    print(f"number = {number}")
    print(f'number = {number}')
    # f - sting alignment
    print(f'{"test":_^22}')  # '_______test_______'
    print(f'{"test":_<22}')  # 'test______________'
    print(f'{"test":_>22}')  # '______________test'
    print(" __________________________________________________________________________________________________________________________________  f-sting python 문자열 포매팅 e")
    print(" __________________________________________________________________________________________________________________________________  데이터의 정렬 s")
    # 파이썬 3.6 버전부터는 자동으로 정렬을 해주므로 OrderedDict를 사용할 필요는 없다.
    from collections import OrderedDict
    od = OrderedDict()
    od['a'] = 'app'
    od['b'] = 'bow'
    od['c'] = 'cow'
    print(od)
    keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    vals = ['app', 'bow', 'cow', 'doc', 'err', 'fly', 'gpu']
    od = OrderedDict((key, val) for key, val in zip(keys, vals))
    print(od)
    print(" __________________________________________________________________________________________________________________________________  데이터의 정렬 e")


magical_words = {
    'as_str': 'as_str',
    'as_list': 'as_list',
    'and_do_nothing': 'and_do_nothing',
    'and_get_it': 'and_get_it',
    'and_print': 'and_print',
    'void': 'void',
    'return': 'return',
    'print': 'print',
    1: 1,
    2: 2,
    3: 3,
}


def chdir(path):
    os.chdir(path)


def dir():
    for i in os.listdir():
        # print(i, end = " ")
        print(i)


def mkdir(path):
    os.mkdir(path)


def mktree(path):
    os.mkdirs(path)


def get_length_of_mp3(target_address):
    try:
        audio = MP3(target_address)
        # print(audio.info.length)
        return audio.info.length
    except:
        print('get_length_of_mp3 메소드에서 에러가 발생하였습니다')


def tasklist():
    for proc in psutil.process_iter():
        try:
            process_im_name = proc.name()
            processID = proc.pid
            print(process_im_name, ' - ', processID)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
            pass


def taskkill(target_str):
    # target_str = 'Music.UI.exe'
    for proc in psutil.process_iter():
        try:
            process_im_name = proc.name()
            processID = proc.pid
            # print(process_im_name , '          - ', processID)

            if process_im_name.strip() == target_str:
                parent_pid = processID
                parent = psutil.Process(parent_pid)
                for child in parent.children(recursive=True):
                    child.kill()
                parent.kill()
                # print(target_str+' 와 자식 프로세스 죽이기를 시도했습니다')

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):  # 예외처리
            pass


def startRecordCommand(file_address):
    # sys.stdout = open('py cmd recording.txt', 'a', encoding='utf-8')  #
    # sys.stdout = open('py cmd recording.txt', 'w', encoding='utf-8')  #
    # sys.stdout = open('py cmd recording.txt', 'r', encoding='utf-8')  #
    sys.stdout = open(file_address, 'w', encoding='utf-8')  #


def endRecordCommand():
    sys.stdout.close()


def saveFileAs(fileAddress):
    startRecordCommand(fileAddress)
    print("이것은 param 두개가 더 필요해 보입니다.")
    endRecordCommand()


def readFile(fileAddress):
    with open(fileAddress, 'r', encoding='utf-8') as f:
        readed_text = f.read()
    return readed_text


def pause():
    os.system("pause")


def listen(recognizer, audio):
    pass


print(" __________________________________________________________________________________________________________________________________  time initialization] ")


def get_time_as_style(time_style):
    now = time
    localtime = now.localtime()
    if time_style == '0':
        default = str(now.strftime('%Y_%m_%d_%H_%M_%S').replace('_', " "))
        return default
    elif time_style == '1':
        timestamp = str(now.time())
        return timestamp
    elif time_style == '2':
        yyyy_MM_dd_HH_mm_ss = str(now.strftime('%Y_%m_%d_%H_%M_%S'))
        return yyyy_MM_dd_HH_mm_ss
    elif time_style == '3':
        customTime1 = str(now.strftime('%Y-%m-%d %H:%M:%S'))
        return customTime1
    elif time_style == '4':
        office_style = str(now.strftime('%Y-%m-%d %H:%M'))
        return office_style
    elif time_style == '5':
        yyyy = str(localtime.tm_year)
        return yyyy
    elif time_style == '6':
        MM = str(localtime.tm_mon)
        return MM
    elif time_style == '7':
        dd = str(localtime.tm_mday)
        return dd
    elif time_style == '8':
        HH = str(localtime.tm_hour)
        return HH
    elif time_style == '9':
        mm = str(localtime.tm_min)
        return mm
    elif time_style == '10':
        ss = str(localtime.tm_sec)
        return ss
    elif time_style == '11':
        weekday = str(localtime.tm_wday)
        return weekday
    elif time_style == '12':
        elapsedDaysFromJan01 = str(localtime.tm_yday)
        return elapsedDaysFromJan01


def AI_Crawlweb(dataWebLocation, copied_html_selector):
    dataWebLocation = unquote(dataWebLocation)  # url decoding
    page = requests.get(dataWebLocation)
    soup = bs(page.text, "html.parser")

    # AI_print(page.text.split('\n'))#전체페이지를 본다

    elements = soup.select(copied_html_selector)
    for index, element in enumerate(elements, 1):
        # print("{} 번째 text: {}".format(index, element.text))
        continue

    return str(element.text)


print(" __________________________________________________________________________________________________________________________________  AI_respon] ")


def AI_respon(usr_input_txt):
    if usr_input_txt == 'pass':
        pass

    elif usr_input_txt == 'x':
        AI_speak('fake AI 를 종료합니다')
        exit()

    elif usr_input_txt == '미세먼지랭킹':
        # AI_speak('미세먼지랭킹 날씨 정보를 디스플레이 시도합니다')
        # AI_run('https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103')
        # AI_speak('시도완료했습니다')
        # AI_speak('미세먼지랭킹 날씨 정보에 접근을 시도합니다')
        # AI_speak('미세먼지랭킹 정보 접근 시도')
        # AI_speak('미세먼지랭킹 정보')
        AI_run('https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103')

    elif usr_input_txt == '종합날씨':
        AI_run('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8')

    elif usr_input_txt == 'taskkill(알송)':
        taskkill('ALSong.exe')
        taskkill('Alsong.exe')

    elif usr_input_txt == '시간':
        yyyy = get_time_as_style('5')
        MM = get_time_as_style('6')
        dd = get_time_as_style('7')
        HH = get_time_as_style('8')
        mm = get_time_as_style('9')
        ss = get_time_as_style('10')
        AI_speak('현재 시간은')
        AI_speak(yyyy + '년')
        AI_speak(MM + '월')
        AI_speak(dd + '일')
        AI_speak(HH + '시')
        AI_speak(mm + '분')
        AI_speak(ss + '초')
        AI_speak('입니다')
        pass

    elif usr_input_txt == '초미세먼지':
        # AI_speak('네이버 초미세먼지 정보 웹크롤링을 시도합니다.')
        dataWebLocation = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A0%84%EA%B5%AD%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
        copied_html_selector = '#main_pack > section.sc_new._atmospheric_environment > div > div.api_cs_wrap > div > div:nth-child(3) > div.main_box > div.detail_box'

        lines = "네이버 초미세먼지 정보\n" + AI_Crawlweb(dataWebLocation, copied_html_selector).replace("관측지점 현재 오전예보 오후예보", "",
                                                                                              1).replace("지역별 미세먼지 정보",
                                                                                                         "").strip().replace(
            "서울", "\n서울").replace("경기", "\n경기").replace("인천", "\n인천").replace("강원", "\n강원").replace("세종",
                                                                                                    "\n세종").replace(
            "충북", "\n충북").replace("충남", "\n충남").replace("전남", "\n전남").replace("전북", "\n전북").replace("광주",
                                                                                                    "\n광주").replace(
            "제주", "\n제주").replace("대전", "\n대전").replace("경북", "\n경북").replace("경남", "\n경남").replace("대구",
                                                                                                    "\n대구").replace(
            "울산", "\n울산").replace("부산", "\n부산").replace("     ", " ").replace("\n ", "\n").replace("  ", " ").replace(
            "  ", " ")
        # AI_speak('웹크롤링이 완료되었습니다')
        # AI_speak('서울과 경기도에 대한 초미세먼지 정보를 말씀드립니다')
        AI_speak('서울 경기도 초미세먼지 정보')

        # for line in range(0,len(lines.split('\n'))):
        # AI_speak(lines.split('\n')[line])

        # for line in range(0,len(lines.split(' '))):
        # AI_speak(lines.split(' ')[line].strip())

        for line in range(0, len(lines.split('\n'))):
            if '서울' in lines.split('\n')[line]:
                tmp = lines.split('\n')[line].split(' ')
                for i in range(0, len(tmp) - 3):
                    AI_speak(tmp[i])

            if '경기' in lines.split('\n')[line]:
                tmp = lines.split('\n')[line].split(' ')
                for i in range(0, len(tmp) - 3):
                    AI_speak(tmp[i])



    elif usr_input_txt == '공간':

        # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s
        INFO_NAME = '네이버 지역 정보'
        dataWebLocation = 'https://weather.naver.com/'
        copied_html_selector = '#now > div > div.location_info_area > div.location_area > strong'
        # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e

        # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s
        # INFO_NAME='구글 지역 정보'
        # dataWebLocation = "https://www.google.com/search?q=%EA%B8%B0%EC%98%A8&oq=%EA%B8%B0%EC%98%A8&aqs=chrome..69i57j35i39j46i131i199i433i465i512j0i131i433i512l3j46i199i465i512j69i61.1706j1j7&sourceid=chrome&ie=UTF-8"
        # copied_html_selector = '#oFNiHe > div > div > div > div.eKPi4 > span.BBwThe'
        # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e

        # AI_speak(INFO_NAME+nbsp+'웹크롤링을 시도합니다')
        # AI_speak('웹크롤링이 완료되었습니다')
        # AI_speak('현재위치에 대한 정보를 말씀드립니다')
        lines = AI_Crawlweb(dataWebLocation, copied_html_selector)
        # AI_print(lines)
        # print(lines)
        # AI_speak(INFO_NAME +'크롤링 결과를 말씀드립니다')
        AI_speak(INFO_NAME + '는')
        AI_speak(lines.strip())
        AI_speak('인 것으로 추측됩니다')


    elif usr_input_txt == '체감온도':  # [웹 스크랩핑 및 유효텍스트 파싱]

        # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s
        INFO_NAME = '네이버 체감온도 정보'
        dataWebLocation = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8'
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
        # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e

        # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s # 구글 지역 정보 option s
        # INFO_NAME='구글 체감온도 정보'
        # dataWebLocation = ''
        # copied_html_selector = ''
        # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e # 구글 지역 정보 option e

        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")

        # AI_print(page.text.split('\n'))#전체페이지를 본다

        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)

        AI_speak(INFO_NAME + '는')
        AI_speak(element_str.strip())
        AI_speak('인 것으로 추측됩니다')

    elif usr_input_txt == '미세먼지':
        try:
            print(" __________________________________________________________________________________________________________________________________  미세먼지] ")
            INFO_NAME = '미세먼지랭킹 미세먼지 정보'
            dataWebLocation = 'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
            dataWebLocation = unquote(dataWebLocation)  # url decoding
            selenium_browser_mgr = webdriver.Chrome()
            # 이 주석은 '첫한글자_유실예방코드' 입니다>첫한글자_유실현상발견>원인분석실패>비온전대응
            selenium_browser_mgr.get(dataWebLocation)
            selenium_browser_mgr.implicitly_wait(5)
            selenium_browser_mgr.switch_to_frame('ifram id 를 수집해서 여기에 작성')

            time.sleep(random.uniform(3, 5))
            selenium_browser_mgr.find_element_by__xpath('').click()

            time.sleep(random.uniform(1, 2))
            print(selenium_browser_mgr.find_element_by__xpath('').text)

            # time.sleep(random.uniform(4, 5))
            selenium_browser_mgr.quit()

            # print(element_str)
            AI_speak('미세먼지')
            # AI_speak(element_str.strip())
        except Exception as e:
            print(' __________________________________________________________________________________________________________________________________  trouble shooting info s')
            traceback.print_exc(file=sys.stdout)
            print(e)
            print(' __________________________________________________________________________________________________________________________________  trouble shooting info e')
            AI_speak('익셉션이 발생하였습니다')


    elif usr_input_txt == '위드비전 근태관리':
        try:
            print(" __________________________________________________________________________________________________________________________________  근태관리] ")
            INFO_NAME = '미세먼지랭킹 미세먼지 정보'
            web_path = 'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
            # web_path = unquote(web_path)  # url decoding
            selenium_browser_mgr = webdriver.Chrome()
            selenium_browser_mgr.implicitly_wait(5)
            selenium_browser_mgr.get(web_path)
            selenium_browser_mgr.switch_to_frame('ifram id 를 수집해서 여기에 작성')

            time.sleep(random.uniform(1, 2))
            selenium_browser_mgr.find_elements_by__css_selector('id').send_keys("pjh4139")
            selenium_browser_mgr.find_element_by_id_('pw').send_keys("비밀번호")

            time.sleep(random.uniform(3, 5))
            selenium_browser_mgr.find_element_by__xpath('').click()

            time.sleep(random.uniform(3, 5))
            selenium_browser_mgr.find_element_by__xpath('').click()

            time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            selenium_browser_mgr.find_element_by_id_('pw').submit()

            time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            # driver.find_element_by_id_("log.login").click()

            print(' __________________________________________________________________________________________________________________________________  captcha alternative 1 s')
            # input_js = ' \
            #         document.getElement_by_id_("id").value = "{id}"; \
            #         document.getElement_by_id_("pw").value = "{pw}"; \
            #     '.format(id="test_id", pw="test_pw")
            # time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            # driver.execute_script(input_js)
            #
            # time.sleep(random.uniform(1, 3))  # 자동화탐지를 우회 하기 위한 delay
            # driver.find_element_by_id_("log.login").click()
            print(' __________________________________________________________________________________________________________________________________  captcha alternative 1 e')

            time.sleep(random.uniform(1, 2))
            print(selenium_browser_mgr.find_element_by__xpath('').text)

            # 기존 scrollHeight를 저장
            last_height = selenium_browser_mgr.execute_script("return document.body.scrollHeight")
            while True:
                # Scroll down
                selenium_browser_mgr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                # page loading를 위한 대기 시간
                time.sleep(random.uniform(1.5, 2))  # Feed를 불러올 수 있도록 램덤 대기
                # 기존 height하고 변화가 발생하지 않을시 break
                new_height = selenium_browser_mgr.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
                last_height = new_height

            # time.sleep(random.uniform(4, 5))
            selenium_browser_mgr.quit()

            # print(element_str)
            AI_speak('미세먼지')
            # AI_speak(element_str.strip())
        except Exception as e:
            print(' __________________________________________________________________________________________________________________________________  trouble shooting info s')
            traceback.print_exc(file=sys.stdout)
            print(' __________________________________________________________________________________________________________________________________  trouble shooting info e')
            AI_speak('익셉션이 발생하였습니다')

    elif usr_input_txt == '종합날씨정보':

        # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s # 네이버 지역 정보 option s
        INFO_NAME = '네이버 종합날씨정보 정보'
        dataWebLocation = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8'
        # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e # 네이버 지역 정보 option e

        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")

        print(" __________________________________________________________________________________________________________________________________  전체페이지 출력 시도] ")
        AI_print(page.text.split('\n'))

        print(" __________________________________________________________________________________________________________________________________  기온] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
        elements = soup.select(copied_html_selector)

        soup.prettify()

        print(str(soup))

        print(str(soup.prettify()))

        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip()
        print(element_str)
        AI_speak('기온')
        AI_speak(element_str.strip().replace('°', ''))
        AI_speak('도')
        print(" __________________________________________________________________________________________________________________________________  현재온도] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.weather_graphic > div.temperature_text > strong'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip().replace('현재 온도', '')
        print(element_str)
        AI_speak('현재온도')
        AI_speak(element_str.replace('°', ''))
        AI_speak('도')
        print(" __________________________________________________________________________________________________________________________________  체감온도] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip()
        print(element_str)
        AI_speak('체감온도')
        AI_speak(element_str.replace('°', ''))
        AI_speak('도')
        print(" __________________________________________________________________________________________________________________________________  습도] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(4)'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text.strip()
        print(element_str)
        AI_speak('습도')
        AI_speak(element_str.replace('%', ''))
        AI_speak('퍼센트')
        print(" __________________________________________________________________________________________________________________________________  바람] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(6)'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        AI_speak('바람')
        AI_speak(element_str.strip().replace('m/s', ''))
        AI_speak('미터퍼세크')
        print(" __________________________________________________________________________________________________________________________________  자외선] ")
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div.report_card_wrap > ul > li.item_today.level2 > a > span'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        AI_speak('자외선')
        AI_speak(element_str.strip())
        print(" __________________________________________________________________________________________________________________________________  미세먼지] ")
        # 미세먼지랭킹 미세먼지 정보 s# 미세먼지랭킹 미세먼지 정보 s# 미세먼지랭킹 미세먼지 정보 s# 미세먼지랭킹 미세먼지 정보 s
        INFO_NAME = '미세먼지랭킹 미세먼지 정보'
        dataWebLocation = 'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
        # 미세먼지랭킹 미세먼지 정보 e # 미세먼지랭킹 미세먼지 정보 e # 미세먼지랭킹 미세먼지 정보 e # 미세먼지랭킹 미세먼지 정보 e
        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")
        copied_html_selector = '#body_main > table:nth-child(7) > tbody > tr:nth-child(2) > td:nth-child(1) > div'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        AI_speak('미세먼지')
        AI_speak(element_str.strip().replace('m/s', ''))
        print(" __________________________________________________________________________________________________________________________________  초미세먼지] ")
        copied_html_selector = '#body_main > table:nth-child(7) > tbody > tr:nth-child(2) > td:nth-child(2) > div'
        elements = soup.select(copied_html_selector)
        for index, element in enumerate(elements, 1):
            # print("{} 번째 text: {}".format(index, element.text))
            continue
        element_str = element.text
        print(element_str)
        AI_speak('초미세먼지')
        AI_speak(element_str.strip())
        AI_speak('입니다')

        # print(" __________________________________________________________________________________________________________________________________  _________] ")
        # copied_html_selector = '_________'
        # elements = soup.select(copied_html_selector)
        # AI_print(elements)#추출된 elements 출력 시도

    elif usr_input_txt == 'hardcode json 처리':
        print(" __________________________________________________________________________________________________________________________________  json 처리 시작] ")
        INFO_NAME = '네이버 체감온도 정보'
        dataWebLocation = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%98%A8'
        copied_html_selector = '#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div._today > div.temperature_info > dl > dd:nth-child(2)'

        dataWebLocation = unquote(dataWebLocation)  # url decoding
        page = requests.get(dataWebLocation)
        soup = bs(page.text, "html.parser")

        copied_html_selector = '_________'
        elements = soup.select(copied_html_selector)
        AI_speak(INFO_NAME + '는')
        AI_speak('인 것으로 추측됩니다')


    elif usr_input_txt == '네이버 미세먼지':
        AI_speak('네이버 미세먼지 정보 웹크롤링을 시도합니다.')
        dataWebLocation = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A0%84%EA%B5%AD%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
        copied_html_selector = '#main_pack > section.sc_new._atmospheric_environment > div > div.api_cs_wrap > div > div:nth-child(3) > div.main_box > div.detail_box'

        lines = "네이버 미세먼지정보\n" + AI_Crawlweb(dataWebLocation, copied_html_selector).replace("관측지점 현재 오전예보 오후예보", "",
                                                                                            1).replace("지역별 미세먼지 정보",
                                                                                                       "").strip().replace(
            "서울", "\n서울").replace("경기", "\n경기").replace("인천", "\n인천").replace("강원", "\n강원").replace("세종",
                                                                                                    "\n세종").replace(
            "충북", "\n충북").replace("충남", "\n충남").replace("전남", "\n전남").replace("전북", "\n전북").replace("광주",
                                                                                                    "\n광주").replace(
            "제주", "\n제주").replace("대전", "\n대전").replace("경북", "\n경북").replace("경남", "\n경남").replace("대구",
                                                                                                    "\n대구").replace(
            "울산", "\n울산").replace("부산", "\n부산").replace("     ", " ").replace("\n ", "\n").replace("  ", " ").replace(
            "  ", " ")
        # print(lines.replace("관측지점 현재 오전예보 오후예보","관측지점 현재 오전예보 오후예보\n"))
        # AI_speak('웹 크롤링된 네이버 미세먼지 정보 접근을 시도합니다.')
        # AI_speak('네이버 미세먼지 정보입니다')
        # AI_speak('다음은 네이버 미세먼지 정보입니다')
        # AI_speak('관측지점 현재 오전예보 오후예보')
        # AI_speak('웹 크롤링된 네이버 미세먼지 정보를 말씀드립니다')
        AI_speak('웹크롤링이 완료되었습니다')
        AI_speak('서울과 경기도에 대한 정보를 말씀드립니다')

        # for line in range(0,len(lines.split('\n'))):
        # AI_speak(lines.split('\n')[line])

        # for line in range(0,len(lines.split(' '))):
        # AI_speak(lines.split(' ')[line].strip())

        for line in range(0, len(lines.split('\n'))):
            if '서울' in lines.split('\n')[line]:
                tmp = lines.split('\n')[line].split(' ')
                for i in range(0, len(tmp) - 3):
                    AI_speak(tmp[i])

            if '경기' in lines.split('\n')[line]:
                tmp = lines.split('\n')[line].split(' ')
                for i in range(0, len(tmp) - 3):
                    AI_speak(tmp[i])

    elif usr_input_txt == '가용코드목록':
        AI_print(AI_available_cmd_code_list)
        AI_speak("조회되었습니다")

    # elif usr_input_txt == 'voiceless mode':
    # def AI_speak(text):
    # print(text)

    # elif usr_input_txt == 'voice mode':
    # def AI_speak(text):
    # address=os.getcwd()+'\\mp3\\'+ text +'.mp3'

    # if os.path.exists(address):
    # os.system('call "'+address+'"')
    # length_of_mp3 = get_length_of_mp3(address)
    # length_of_mp3 = float(length_of_mp3)
    # length_of_mp3 = round(length_of_mp3,1)
    # time.sleep(length_of_mp3*1.05)

    # else:
    # mgr_gTTS = gTTS(text=text, lang='ko')
    # mgr_gTTS.save('./mp3/'+ text +'.mp3')
    # os.system('call "'+address+'"')

    # length_of_mp3 = get_length_of_mp3(address)
    # length_of_mp3 = float(length_of_mp3)
    # length_of_mp3 = round(length_of_mp3,1)
    # time.sleep(length_of_mp3*1.05)

    # taskkill('ALSong.exe')

    # elif usr_input_txt == '`':
    #     AI_speak('single mode 가 시작되었습니다')
    #     # print('single mode s single mode s single mode s single mode s single mode s single mode s single mode s single mode s single mode s ')
    #     while(True):
    #         batch_mode_input=input('>>>')
    #         if batch_mode_input =='x':
    #             AI_speak('single mode를 종료합니다')
    #             break
    #         elif len(batch_mode_input)==1:
    #             usr_input_txt=AI_available_cmd_code_list[int(batch_mode_input)-1].split(':')[0]
    #             AI_respon(usr_input_txt)
    #         elif batch_mode_input =='':
    #             AI_speak('아무것도 입력되지 않았습니다')
    #         elif batch_mode_input =='`':
    #             AI_speak('백팁은 single mode에서 입력하실 수 없습니다.')
    #         else:
    #             AI_speak('single mode 에서는 1자리만 입력하실 수 있습니다.')
    #     # print('eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e eingle mode e ')
    #

    # elif usr_input_txt == '``':
    #     AI_speak('batch mode 가 시작되었습니다')
    #     # print('batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s batch mode s ')
    #     while(True):
    #         batch_mode_input=input('>>>')
    #         if batch_mode_input=='x' or batch_mode_input=='X' :
    #             AI_speak('batch mode를 종료합니다')
    #             break
    #         # batch_mode_input=list(batch_mode_input)                         # batch_mode_input = [3,2,1]
    #         # AI_speak('입력된 배치명령의 개수는' + str(len(batch_mode_input)+1) +'개 입니다')
    #         if batch_mode_input == '':
    #             AI_speak('아무것도 입력되지 않았습니다')
    #             AI_speak('명령코드를 입력해주세요')
    #         else:
    #             AI_speak('입력된 배치명령의 개수는' + str(len(batch_mode_input)) +'개 입니다')
    #             for i in range(0,len(batch_mode_input)):                      # i=0
    #                 usr_input_txt=AI_available_cmd_code_list[int(batch_mode_input[i])-1].split(':')[0] #usr_input_txt=AI_available_cmd_code_list[2].split(':')[0]
    #                 AI_speak(str(i+1)+'번째 코드를 실행시도합니다')
    #                 AI_respon(usr_input_txt)
    #
    #     # print('batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e batch mode e ')

    elif usr_input_txt == '`':
        AI_speak('advanced batch mode 가 시작되었습니다')
        print(
            'advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s advanced batch mode s')
        cls()
        print("")
        print("")
        print("")
        print("")
        # print(' '+'가용명령코드목록')
        print('                                     ' + '가용명령코드목록')
        print("")
        AI_print(AI_available_cmd_code_list)
        print("")
        while (True):
            batch_mode_input = input(
                "                                                                                                ")
            if batch_mode_input == 'x' or batch_mode_input == 'X':
                AI_speak('advanced batch mode를 종료합니다')
                break
            elif batch_mode_input == '':
                AI_speak('아무것도 입력되지 않았습니다')
                AI_speak('명령코드를 입력해주세요')
            else:
                list = batch_mode_input.split(' ')
                # AI_speak('입력된 코드 목록 입니다')
                # for str in list:
                #     AI_speak(str)
                # for i in range(0,len(list)-2):
                for list_element in list:
                    # AI_speak(str((i+1))+'번째 코드를 실행시도합니다')
                    # print(list[i])
                    # AI_respon(str(list[i]))
                    # if len(AI_available_cmd_code_list)<AI_available_cmd_code_list[int(list[i])-1].split(':')[0]:
                    # AI_respon(AI_available_cmd_code_list[int(list[i])-1].split(':')[0])
                    # print(list_element)
                    # for i in range(0, len(AI_available_cmd_code_list) - 1):
                    #     if usr_input_txt in AI_available_cmd_code_list[i].split(':')[0]:
                    #         # if usr_input_txt!='' or usr_input_txt!='`':
                    #         if usr_input_txt != '':
                    #             # AI_speak(AI_available_cmd_code_list[i].split(':')[0]+'에 대한 명령코드가 입력되었습니다')
                    #             pass
                    #
                    # AI_respon(usr_input_txt)
                    # try:
                    # print(len(AI_available_cmd_code_list[int(list_element) - 1]))
                    # print(AI_available_cmd_code_list[int(list_element) - 1])
                    # AI_speak(AI_available_cmd_code_list[int(list_element) - 1].split(':')[0])
                    try:
                        AI_respon(AI_available_cmd_code_list[int(list_element) - 1].split(':')[0])
                    except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
                        AI_speak('advanced batch mode 실행 중 예외가 발생했습니다')
                        print('advanced batch mode 실행 중 예외가 발생했습니다')
                        print(e)
                        # AI_speak('가용코드 목록에 없는 코드입니다')

        print(
            'advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e advanced batch mode e')


    elif usr_input_txt == '가용명령개수':
        AI_speak('가용명령의 개수는')
        AI_speak(str(len(AI_available_cmd_code_list)))
        AI_speak('개 입니다')
        AI_respon('3 ')

    elif usr_input_txt == '식물조언':
        AI_speak('식물에게 물샤워를 줄시간입니다')
        AI_speak('물샤워를 시켜주세요')
        AI_speak('오늘은 식물에게 햇빛샤워를 시켜주는날입니다')
        AI_speak('하늘이가 없을때 샤워를 시켜주세요')
        AI_speak('하트축전에게 빠르게 식물등빛을 주세요')
        AI_speak('이러다 죽습니다')
        AI_speak('서둘러 등빛을 주세요')

    elif usr_input_txt == '':
        AI_speak('아무것도 입력되지 않았습니다')
        AI_speak('명령코드를 입력해주세요')

    elif usr_input_txt == '몇 시야' or usr_input_txt == '몇시야':
        # AI_speak(get_time_as_style('5'))
        # AI_speak('년')
        # AI_speak(get_time_as_style('6'))
        # AI_speak('월')
        # AI_speak(get_time_as_style('7'))
        # AI_speak('일')
        AI_speak(get_time_as_style('8'))
        AI_speak('시')
        AI_speak(get_time_as_style('9'))
        AI_speak('분')
        AI_speak('입니다')

    elif usr_input_txt == 'jhppc1':
        jhppc1 = 'https://remotedesktop.google.com/access/session/b797cd99-b738-f4db-9b38-9a2e25a57a47'
        AI_run(jhppc1)

    elif usr_input_txt == 'remotedesktop':
        remotedesktop = 'https://remotedesktop.google.com/access'
        AI_run(remotedesktop)

    elif usr_input_txt == 'sd_s':
        ment = "정말로 컴퓨터를 종료할까요 원하시면 Y를 눌러주세요"
        AI_speak(ment)
        usr_input_txt = input(ment)
        if usr_input_txt.upper() == 'Y':
            ment = '시스템 종료를 시도합니다'

            # AI_speak('1시간 뒤 s')
            AI_speak(ment)
            # os.system('shutdown /s /t 3600')  # 1시간 뒤
            # AI_speak('1시간 뒤 e')

            # AI_speak('즉시 s')
            AI_speak(ment)
            os.system('shutdown /s /t 0')  # 즉시
            # AI_speak('즉시 e')

            # AI_speak('10분 뒤')
            AI_speak(ment)
            # os.system('shutdown /s /t 600') #10분 뒤
            # AI_speak('10분 뒤')
        else:
            pass

    elif usr_input_txt == 'sd_e':
        os.system('chcp 65001')
        # os.system('cmd /k shutdown -a')
        os.system('cmd /k shutdown -a > tmp.txt')
        os.system('echo 아래의 명령어를 사용하여 cmd를 종료하여 되돌아 갈 수 있습니다')
        os.system('echo exit()')

    elif usr_input_txt == 'cls()':
        cls()

    elif usr_input_txt == '스케쥴 모드':
        AI_speak('스케쥴 모드를 시작합니다')
        cnt = 0
        started_time = 0
        while (True):

            yyyy = get_time_as_style('5')
            MM = get_time_as_style('6')
            dd = get_time_as_style('7')
            HH = get_time_as_style('8')
            mm = get_time_as_style('9')
            ss = get_time_as_style('10')

            if cnt == 0:
                # AI_speak('while routine에 접근을 시도합니다')
                started_time = get_time_as_style('0')
                # AI_speak('컴퓨터와 대화할 준비가 되었습니다')
                # taskkill('ALSong.exe')
                cnt += 1
                cls()

            if ss == '30':
                # 5분마다 말하기 s
                # if int(mm)%'05'==0:
                # AI_speak('현재 시간은')
                # AI_speak(HH+'시')
                # AI_speak(mm+'분')
                # AI_speak('입니다')
                # 5분마다 말하기 e

                # 10분마다 말하기 s
                # if int(mm)%'10'==0:
                # AI_speak('현재 시간은')
                # AI_speak(HH+'시')
                # AI_speak(mm+'분')
                # AI_speak('입니다')
                # 10분마다 말하기 e

                # 9시에서 11시 사이에는 15분마다 말하기 s
                # if 9 <= int(HH) and int(HH) <= 23 and int(mm) % 15 == 0:
                if 9 <= int(HH) <= 23 and int(mm) % 15 == 0:  # 파이썬은 간결하게 이런것도 됩니다
                    AI_speak('현재 시간은')
                    AI_speak(HH + '시')
                    AI_speak(mm + '분')
                    AI_speak('입니다')
                # 9시에서 11시 사이에는 15분마다 말하기 e

                # 아침 6시 부터는 5분마다 시간 말하기 s
                if HH == '06' and int(mm) % 5 == 0:
                    AI_speak('현재 시간은')
                    AI_speak(HH + '시')
                    AI_speak(mm + '분')
                    AI_speak('입니다')
                # 아침 6시 부터는 5분마다 시간 말하기 e

                # 아침 7시 부터는 5분마다 시간 말하기 s
                if HH == '07' and int(mm) % 5 == 0:
                    AI_speak('현재 시간은')
                    AI_speak(HH + '시')
                    AI_speak(mm + '분')
                    AI_speak('입니다')
                # 아침 7시 부터는 5분마다 시간 말하기 e

                # 아침 8시에 시간 말하기 s
                if HH == '08' and mm == '00':
                    AI_speak('현재 시간은')
                    AI_speak(HH + '시')
                    AI_speak(mm + '분')
                    AI_speak('입니다')
                    AI_speak('더이상 나가는 것을 지체하기 어렵습니다')
                # 아침 8시에 시간 말하기 e

                # 아침 6시에 30분에 음악재생하기
                if HH == '06' and mm == '30':
                    AI_speak('음악을 재생합니다')
                    AI_run()
                    # [TO DO]

                if HH == '08' and mm == '50':
                    AI_speak('업무시작 10분전입니다')
                    AI_speak('업무준비를 시작하세요')
                    # [TO DO]

                if HH == '09' and mm == '00':
                    AI_speak('음악을 종료합니다')
                    # taskkill('Music.UI.exe')
                    # taskkill('ALSong.exe')
                    # time.sleep(10)
                    # [TO DO]

                if HH == '11' and mm == '30':
                    AI_speak('점심시간입니다')
                    # [TO DO]

                if HH == '11' and mm == '30':
                    AI_speak('음악을 재생합니다')
                    # [TO DO]

                if HH == '11' and mm == '30':
                    AI_speak('12시 30분 입니다')
                    AI_speak('씻으실 것을 추천드립니다')
                    AI_speak('샤워루틴을 수행하실 것을 추천드립니다')
                    # AI_speak('샤워루틴을 보조를 수행할까요')
                    # [TO DO]

                if HH == '11' and mm == '50':
                    AI_speak('12시 10분 전입니다')
                    AI_speak('누우실 것을 추천드립니다')
                    # AI_speak('주무실 것을 추천드립니다')
                    # [TO DO]

                # 30분 마다 랜덤기기(뽑기)를 의도한 수 나오면 프로그램 시작 경과시간 말하기
                if mm % 30 == 0:
                    go_or_no_go = random.randrange(1, 101)  # 1에서 100 사이의 수
                    if go_or_no_go == 55 or 58 or 100:
                        AI_speak('랜덤 수와 의도한 수가 일치합니다')

                        print('프로그램을 시작시간은')
                        print(started_time.split(' ')[0])  # 년
                        print('년')
                        print(started_time.split(' ')[1])  # 월
                        print('월')
                        print(started_time.split(' ')[2])  # 일
                        print('일')
                        print(started_time.split(' ')[3])  # 시
                        print('시')
                        print(started_time.split(' ')[4])  # 분
                        print('분')
                        print(started_time.split(' ')[5])  # 초

                        print('프로그램을 현재시각은')
                        print(yyyy)  # 년
                        print('년')
                        print(MM)  # 월
                        print('월')
                        print(dd)  # 일
                        print('일')
                        print(HH)
                        print('시')
                        print(mm)
                        print('분')

                        AI_speak('프로그램을 경과시각은')  # 경과일  ,   경과시각,   경과분,  모두 연산이 고민이 필요한 것 같다
                        delta_yyyy = str(float(yyyy) - float(started_time.split(' ')[0]))
                        AI_speak(delta_yyyy + '년')

                        delta_MM = str(float(MM) - float(started_time.split(' ')[1]))
                        AI_speak(delta_MM + '월')

                        delta_dd = str(float(dd) - float(started_time.split(' ')[2]))
                        AI_speak(delta_dd + '일')

                        delta_HH = str(float(HH) - float(started_time.split(' ')[3]))
                        AI_speak(delta_HH + '시')

                        delta_mm = str(float(mm) - float(started_time.split(' ')[4]))
                        AI_speak(delta_mm + '분')

                        AI_speak('프로그램을 시작한지')
                        AI_speak(delta_yyyy + '년')
                        AI_speak(delta_MM + '월')
                        AI_speak(delta_dd + '일')
                        AI_speak(delta_HH + '시')
                        AI_speak(delta_mm + '분')
                        AI_speak('으로 추측됩니다')

                        # [TO DO]


    elif usr_input_txt == '_________':
        AI_speak('해당 기능은 아직 준비되지 않았습니다')

    else:
        # AI_speak('입력하신 내용이 usr_input_txt 는 oooo 과 유사합니다') #[to do]
        # AI_speak('해당 기능은 아직 준비되지 않았습니다')
        available_no_cmd_list = []
        try:
            for i in range(0, len(AI_available_cmd_code_list)):
                available_no_cmd_list.append(i + 1)

            print(available_no_cmd_list)

            if int(usr_input_txt) in available_no_cmd_list:
                # AI_speak(str(available_no_cmd_list)+' 중에 하나라면 실행 가능한 코드입니다')
                # AI_speak(usr_input_txt+' 가용목록 인덱스가 입력되었습니다.')
                AI_speak('가용목록 인덱스가 입력되었습니다.')
                AI_speak('인덱스에 대한 코드를 수행합니다')

                # [TO_DO s]
                AI_speak(
                    '이 다음코드는 더이상 진행되지 않게. 루프의 처음부분으로 돌아가도록 리턴을 시키는 임시대응코드 입니다. 추후에 삭제를 하고. 엔덱스에 따라 작동하도록 다른 것으로 대체할 것 입니다')
                usr_input_txt = 'pass'
                # [TO_DO e]

            else:
                pass

        except Exception as e:
            print(' __________________________________________________________________________________________________________________________________  trouble shooting info s')
            traceback.print_exc(file=sys.stdout)
            print(' __________________________________________________________________________________________________________________________________  trouble shooting info e')
            AI_speak(
                '익셉션이 발생하였습니다. 익셉션을 발생시키고 넘어가도록 하는 것은. 익셉션을 발생시키지 않고 처리하는 것보다 좋은 방법은 아닌 것 같습니다. 추후에 수정을 해주세요. 일단은 진행합니다')
            # AI_speak('익셉션이 발생하였습니다')
            # AI_speak('익셉션을 발생시키고 넘어가도록 하는 것은 익셉션을 발생시키지 않고 처리하는 것보다 좋은 방법은 아닌 것 같습니다')
            # AI_speak('추후에 수정을 해주세요')
            # AI_speak('일단은 진행합니다')


def AI_speak(text):
    # address=r""+os.getcwd()+'\\mp3\\음성인식 준비되었습니다.mp3'
    # address=u""+os.getcwd()+'\\mp3\\음성인식 준비되었습니다.mp3'
    # address=os.getcwd()+'\\mp3\\음성인식 준비되었습니다.mp3'
    address = os.getcwd() + '\\mp3\\' + text + '.mp3'

    if os.path.exists(address):
        # print('파일이 있어 재생을 시도합니다')
        # os.system('"'+address+'"')#SUCCESS
        os.system('call "' + address + '"')  # SUCCESS[경로공백포함 시 인식처리]

        # mp3 파일의 재생 길이를 알아내서 그 시간만큼 sleep 시키는 코드를 추가[to do]
        length_of_mp3 = get_length_of_mp3(address)
        # print(length_of_mp3)
        length_of_mp3 = float(length_of_mp3)
        # print(length_of_mp3)
        length_of_mp3 = round(length_of_mp3, 1)
        # print(length_of_mp3)
        # time.sleep(length_of_mp3*0.95)
        # time.sleep(length_of_mp3*1.00)
        time.sleep(length_of_mp3 * 1.05)


    else:
        # print('가지고 있는 mp3 파일이 없어 생성을 시도합니다')
        mgr_gTTS = gTTS(text=text, lang='ko')
        mgr_gTTS.save('./mp3/' + text + '.mp3')
        os.system('call "' + address + '"')  # call을 사용해서 동기처리를 기대했으나 되지 않음.대안이 필요하다.

        # mp3 파일의 재생 길이를 알아내서 그 시간만큼 sleep 시키는 코드를 추가[to do]
        length_of_mp3 = get_length_of_mp3(address)
        # print(length_of_mp3)
        length_of_mp3 = float(length_of_mp3)
        # print(length_of_mp3)
        length_of_mp3 = round(length_of_mp3, 1)
        # print(length_of_mp3)
        # time.sleep(length_of_mp3*0.95)
        # time.sleep(length_of_mp3*1.00)
        time.sleep(length_of_mp3 * 1.05)

    taskkill('ALSong.exe')


def AI_run(target_str):
    last_txt = target_str.split('.')[-1]
    if 'http' in target_str:
        if '%' in target_str:
            target_str = 'explorer "' + unquote(target_str).strip() + '"'  # url decoding
            os.system(target_str)
        else:
            os.system('start ' + target_str)
            # os.system('explorer ' + target_str)
            # __________________________________________________________________________________ 방법1 s
            chromeMgr = webdriver.Chrome()
            # 이 주석은 '첫한글자_유실예방코드' 입니다>첫한글자_유실현상발견>원인분석실패>비온전대응
            chromeMgr.get(target_str)
            # __________________________________________________________________________________ 방법1 e

    elif 'txt' in last_txt:
        os.system('start ' + target_str)
        # os.startfile(os.getcwd()+'/mp3/'+ text +'.mp3') #비동기처리방식
        # os.system('call "'+os.getcwd()+'/mp3/'+ text +'.mp3"')  #동기처리방식[실패]

    elif 'mp3' in last_txt:
        os.system('start ' + target_str)

    elif 'mp4' in last_txt:
        os.system('start ' + target_str)
        # [TO DO]


def AI_print(target_list):
    cnt = 1
    for target in target_list:
        # print('+str(cnt)+nbsp+':'+nbsp+target)
        # print('         '+str(cnt)+nbsp+':'+nbsp+target)
        print('                                             ' + str(cnt) + nbsp + ':' + nbsp + target)
        # print("")
        cnt += 1


def convert_path_style(path_str, style_no):
    if style_no == "1":
        if "\\" in path_str:
            path_str = path_str.replace("\\", "/")
            return path_str

    elif style_no == "2":
        if "/" in path_str:
            path_str = path_str.replace("/", "\\")
            return path_str

    elif style_no == "3":
        if "\\\\" in path_str:
            path_str = path_str.replace("\\\\", "\\")
            return path_str

    elif style_no == "4":
        if "//" in path_str:
            path_str = path_str.replace("//", "/")
            return path_str

    elif style_no == "5":
        if "/" in path_str:
            path_str = path_str.replace("/", "//")
            return path_str

    elif style_no == "6":
        if "\\" in path_str:
            path_str = path_str.replace("\\", "\\\\")
            return path_str

    else:
        AI_speak('trouble shooting info id')
        AI_speak('yyyy MM dd HH mm ss')


def get_length_by__using_(______tuple):  # done
    return len(______tuple)


def get_keys_by__using_(______tuple, _____as):
    if _____as == 'as_str':
        return str(______tuple.keys()).replace("dict_keys([", "").replace("])", "").replace("\'", "")
    elif _____as == 'as_list':
        return get_keys_by__using_(______tuple, "as_str").split(", ")
    else:
        print("it is not magical word. so do nothing")


def print_key_with_index_by__using_(______tuple):
    for ______tuple_key in get_keys_by__using_(______tuple, "as_list"):
        print(str(get_keys_by__using_(______tuple, "as_list").index(______tuple_key)) + " " + ______tuple_key)


def get_values_by__using_(______tuple, _____as):
    if _____as == magical_words['as_str']:
        index_cnt = 0
        tmp_str = ""
        for key, value in ______tuple.items():
            if tmp_str != "":
                tmp_str = tmp_str + "\n"
            tmp_str = tmp_str + str(value)
            index_cnt + +1
        return tmp_str
    if _____as == magical_words['as_list']:
        index_cnt = 0
        tmp_list = []
        for key, value in ______tuple.items():
            tmp_list.append(str(value))
            index_cnt + +1
        return tmp_list


def print_index_and_value_and_key_by__using_(______tuple, mode):
    if mode == magical_words[1]:
        index_cnt = 0
        tmp_str = ""
        for key, value in ______tuple.items():
            tmp_str = str(index_cnt) + "\t" + str(key)
            print(tmp_str)
            index_cnt = index_cnt + 1
    elif mode == magical_words[2]:
        index_cnt = 0
        tmp_str = ""
        for key, value in ______tuple.items():
            tmp_str = str(index_cnt) + "\t" + str(value)
            print(tmp_str)
            index_cnt = index_cnt + 1
    elif mode == magical_words[3]:
        index_cnt = 0
        tmp_str = ""
        for key, value in ______tuple.items():
            tmp_str = str(index_cnt) + "\t" + str(key) + "\t" + str(value)
            print(tmp_str)
            index_cnt = index_cnt + 1
    else:
        print("it is not magical word. so do nothing")


def getText_by__using_(_____list, _____mode):
    if _____mode == magical_words["as_tuple"]:
        print("_________________________________________ TBD")


def replace_text_B_and_text_C_interchangeably_at_text_A_by__using_(____text_A, ____text_B, ____text_C, _____and):
    tmp_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
    text_special = "{{no}}"
    text_B_cnt = ____text_A.count(____text_B)
    tmp_list = []
    tmp_str = ""
    tmp_cmt = 0
    if ____text_C == "":
        ____text_A = ____text_A.replace(____text_B, ____text_C)
    elif text_special in ____text_C:
        print("text_A 에서 " + ____text_B + " 를 총" + str(text_B_cnt) + "개 발견하였습니다")
        tmp_list = ____text_A.split(____text_B)
        if ____text_B in ____text_C:
            tmp_cmt = 0
            for j in tmp_list:
                if j == tmp_list[-1]:
                    pass
                else:
                    tmp_str = tmp_str + j + ____text_C.split(text_special)[0] + str(tmp_cmt)
                tmp_cmt = tmp_cmt + 1
            ____text_A = ""
            ____text_A = tmp_str
        else:
            tmp_cmt = 0
            for j in tmp_list:
                if j == tmp_list[-1]:
                    pass
                else:
                    tmp_str = tmp_str + j + ____text_C.split(text_special)[0] + str(tmp_cmt)
                tmp_cmt = tmp_cmt + 1
            ____text_A = ""
            ____text_A = tmp_str
    else:
        ____text_A = ____text_A.replace(____text_C, tmp_foo)
        ____text_A = ____text_A.replace(____text_B, ____text_C)
        ____text_A = ____text_A.replace(tmp_foo, ____text_B)
    if _____and == magical_words["and_do_nothing"]:  # void mode
        pass
    elif _____and == magical_words["and_get_it"]:  # return mode
        return ____text_A
    elif _____and == magical_words["and_print"]:  # print mode
        print(____text_A)
    else:
        print("it is not magical word. so do nothing")


def act_via_interchangeable_triangle_model_by__using_(____text_A, ____text_B, ____text_C, _____and):
    tmp_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
    if ____text_C == "":
        ____text_A = ____text_A.replace(____text_B, ____text_C)
    else:
        ____text_A = ____text_A.replace(____text_C, tmp_foo)
        ____text_A = ____text_A.replace(____text_B, ____text_C)
        ____text_A = ____text_A.replace(tmp_foo, ____text_B)
    if _____and == magical_words["and_do_nothing"]:  # void mode
        pass
    elif _____and == magical_words["and_get_it"]:  # return mode
        return ____text_A
    elif _____and == magical_words["and_print"]:  # print mode
        print(____text_A)
    else:
        print("it is not magical word. so do nothing")


def pause():
    try:
        print(" __________________________________________________________________________________________________________________________________  code debugging")
        os.system("chcp 65001")
        os.system("pause")
    except Exception as e:
        print(' __________________________________________________________________________________________________________________________________ troubleshooting s')
        traceback.print_exc(file=sys.stdout)
        print(' __________________________________________________________________________________________________________________________________ troubleshooting e')


print(" __________________________________________________________________________________________________________________________________  s")
print(f'''서버 시작 시각            : {get_time_as_style('0')}''')
time_s = time.time()

# :: 웹 서버, DB 서버 API 관련 모듈 설정
from flask import Flask, render_template, jsonify, url_for, request, redirect, abort, flash
from sqlalchemy import create_engine, text
import pymysql
# import mysql   # pip install mysql 수행 시 error 발생되어 주석처리.
# import config  # config.py 에서 config/__init__.py 로 대체되었음.
# import ssl     #ssl 보안레이어 추가시 사용




print(' __________________________________________________________________________________________________________________________________ flask config 설정 s')
app = Flask(__name__, static_url_path="/static")
# app = Flask(__name__, static_url_path="/static/")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mysql-root@localhost/travel_mate?charset=utf8'
# app.config['SQLALCHEMY_ECHO'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.secret_key = 'many      random     byte'
# app.config.from_pyfile("config.py")  # python 패키지를 만들면 __init__.py 가 생성된다
# app.config.from_object(config)
# app.config.from_envvar('APP_CONFIG_FILE') # 이걸 쓰려면 환경 변수를 추가해야한다. 안그럼 RuntimeError 가 발생  추후에 설정

print(' __________________________________________________________________________________________________________________________________ flask config 설정 e')
#  __________________________________________________________________________________________________________________________________ python web session 설정 s
from flask import session

# random bytes 시크릿 키 비밀번호로 app.secret_key 변수에 저장, 잘 보관해라 이 비밀번호를
app.secret_key = b'f1748cc247d4d2978cda20416015bd551a90561e44e79b2a003a48bd646c4570'
#  __________________________________________________________________________________________________________________________________ python web session 설정 e
#  __________________________________________________________________________________________________________________________________ flask file upload 설정 s
# :: 파일 업로드 위치 설정
app.config['UPLOAD_FOLDER'] = 'uploads/'  #이러면 동작은 되던데?. 의도한건 아니지만.
# app.config['UPLOAD_FOLDER'] = '/uploads/'
# app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# :: 파일 확장자 범위 설정
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip', 'toml'}

# :: 파일 확장자 유효성 확인 설정
def check_allowed_file_or_not(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#  __________________________________________________________________________________________________________________________________ flask file upload 설정 e

# __________________________________________________________________________________________________________________________________ controller s
'''
페이지 라우팅 테스트 페이지
'''
url_paths['url202311100030'] = '/urls-routing-test'
@app.route(url_paths['url202311100030'])
def test_urls_routing():
    if (request.method == 'GET'):  # 해당페이지 의 GET REQUEST 인 경우 수행할 STATEMENTS
        content = f'''
        <html>
            <form name="fm_request"›'''
        for key, value in url_paths.items():
            content += f'''<li><a href="{url_paths[str(key)]}">{url_paths[str(key)]}</a></li> '''
        content += f'''
            </form>
        </html>'''
        return content
    else:
        #POST 요청 시
        abort(401)
        # 서버에서 엑세스 거부 하도록 설정 @app.route 설정이 GET 으로 되어 있어 abort(401)은 도달하지 않을 코드 같다.


'''
에러 페이지
'''
@app.route("/error")
def route20231111132812():
    return render_template("/errors/error_default.html")


# '''
# 개발자 페이지
# '''
# url_paths['url202311110140'] = '/temp'
# @app.route(url_paths['url202311110140'])
# def route2023111110308():
#     return render_template("/developer.html")


# '''
# 관리자 페이지
# '''
# url_paths['url202311110141'] = '/admin'
# @app.route(url_paths['url202311110141'])
# def route2023111110309():
#     return render_template("/admin/main.html")


# '''
# 고객 페이지
# '''
# url_paths['url202311110142'] = '/home'
# @app.route(url_paths['url202311110142'])
# def route2023111110310():
#     return render_template("/home/main.html")


'''
스타팅 페이지 
'''
url_paths['url202311100026'] = '/'


@app.route(url_paths['url202311100026'])
def render_index():
    return redirect(url_paths['url20231111501'])


# mkr
'''
직원 페이지
'''
url_paths['url20231111161629'] = '/employee'


@app.route(url_paths['url20231111161629'])
def route2023111110315():
    # :: session 기간 내에 로그인 했었는지 확인
    if 'id' in session:
        return render_template('/employee/main.html')
    else:
        return render_template('/employee/login.html')


'''
직원 로그인 페이지
'''
url_paths['url20231111501'] = '/employee/login'


@app.route(url_paths['url20231111501'])
def route20231111162108():
    # :: session 기간 내에 로그인 했었는지 확인
    if 'id' in session:
        return redirect(url_paths['url20231111161629'])
    else:
        return render_template('/employee/login.html')


'''
직원 로그인 처리 페이지
'''
url_paths['url202311111423'] = '/employee/login_'


@app.route(url_paths['url202311111423'], methods=['POST'])
def route2023111110312():
    # :: 이전 페이지 데이터 202311121629
    # print(f''':: 이전 페이지 데이터 202311121629''')
    # print(f'''id: {request.form['id']}''')
    # print(f'''pw: {request.form['pw']}''')

    # print(f''' :: 로그인 입력 데이터 validation 2차 확인 로직''')
    # if validate_user_input(request.form['username'],request.form['pw']):
    #     return log_the_user_in(request.form['username'])
    # else:
    #     error = 'Invalid username/password'
    #     return render_template('login.html', error=error)

    # :: DB에 아이디와 PW가 동시에 일치하는 레코드가 있는지 확인
    employees_joined = employee_joined_list.get_employee_joined(id=request.form['id'], pw=request.form['pw'])

    if employees_joined.first() != None:
        print(f''':: 세션에 저장''')
        session['id'] = request.form['id']
        session['login_time'] = get_time_as_style("0")
        for employee_joined in employees_joined:
            print(f'''name: {employee_joined.name}  id: {employee_joined.id}   pw: {employee_joined.pw}''')
            if session['name'] != None:
                session['name'] = employee_joined.name

        content = f'''
        <script>
            alert("로그인 되었습니다")
            setTimeout(function() {{
                window.location.href='{url_paths['url20231111161629']}'  
                // window.close(); 
            }}, 500);
        </script>
        '''
        return content
    else:
        content = f'''
                <script>
                    alert("패스워드 또는 아이디가 틀렸습니다.")
                    //alert("로그인에 실패하였습니다.")
                    setTimeout(function() {{
                        window.location.href='{url_paths['url20231111161629']}'  
                        // window.close(); 
                    }}, 500);
                </script>
                '''
        return content
    #  __________________________________________________________________________________________________________________________________ DB.employee_tb 에서 id /pw 확인 e


'''
직원 로그아웃 페이지
'''
url_paths['url20231111164038'] = '/employee/logout'
@app.route(url_paths['url20231111164038'], methods=['POST'])
def route20231111164103():
    # :: 세션에서 id 제거
    session.pop('id', None)
    return redirect(url_paths['url20231111501'])


'''
직원 회원가입 페이지
'''
url_paths['url202311111421'] = '/employee/join'


@app.route(url_paths['url202311111421'], methods=['POST'])
def route2023111110313():
    return render_template("/employee/join.html")


'''
직원 회원가입 처리 페이지 
'''
url_paths['url202311111424'] = '/employee/join_'


@app.route(url_paths['url202311111424'], methods=['POST'])
def route2023111110314():
    # :: 신규가입시도자아이디 기존가입자아이디 비교
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
        print(f'''중복된 아이디가 있습니다.''')
        flash(f'''중복된 아이디가 있습니다.''')
        return render_template("/employee/join.html")
    print(f'''?''')
    row = cursor.fetchone()  # 데이타 Fetch one 하여 출력, jsp 에서 resultSet 처럼 쓰는 것 같다.
    while row:
        print(row[0], row[1])
        row = cursor.fetchone()
    print(f'''?''')
    cursor.close()
    conn.close()

    # :: 가입조건 확인
    # 직원 회원가입 조건은 아무나 가능

    # :: ORM 사용해서 DB에 저장
    print(f''' :: ORM 사용해서 DB에 저장''')
    employee_joined_list.add_new_records(name=request.form['name'], pw=request.form['pw'], phone_no=request.form['phone_no'], address=request.form['address'], e_mail=request.form['e_mail'], age=request.form['id'], id=request.form['id'], date_joined=get_time_as_style("0"), date_canceled="")

    # :: 회원가입
    return f'''
    <script>
        alert("회원가입 되었습니다")
        setTimeout(function() {{
            window.location.href='{url_paths['url20231111501']}'  
            // window.close(); 
        }}, 0);
    </script>
    '''


'''
직원 출근 처리 페이지
'''
url_paths['url20231111538'] = '/employee/go-to-office'


@app.route(url_paths['url20231111538'], methods=['POST'])
def route2023111110321():
    # :: 세션에서 데이터 가져와서 변수에 저장
    id = session['id']
    name = session['name']

    # :: 서버시간 가져와서 변수에 저장
    HH = get_time_as_style('8')
    mm = get_time_as_style('9')

    return f'''
        <div>{name} 님 {HH}시 {mm}분 출근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='{url_paths['url20231111501']}'  
                // window.close(); 
            }}, 3000);
        </script>
    '''


'''
직원 퇴근 처리 페이지
'''
url_paths['url202311110410'] = '/employee/leave-office'


@app.route(url_paths['url202311110410'], methods=['POST'])
def route202311110410():
    # :: 세션에서 데이터 가져와서 변수에 저장
    id = session['id']
    name = session['name']

    # :: 서버시간 가져와서 변수에 저장
    HH = get_time_as_style('8')
    mm = get_time_as_style('9')

    return f'''
        <div>{name} 님 {HH}시 {mm}분 퇴근처리 되었습니다.</div>
        <script>
            setTimeout(function() {{
                window.location.href='{url_paths['url20231111501']}'  
                // window.close(); 
            }}, 3000);
        </script>
    '''


'''
직원 FAQ 게시판
'''
url_paths['url202311100027'] = '/employee/faq-board'


@app.route(url_paths['url202311100027'], methods=['POST'])
def route2023111110316():
    datas = {
        'id': session['id'],
        'login_time': session['login_time'],
    }
    return render_template('/employee/faq_board.j2', name=datas)


'''
직원 파일 업로드 게시판
'''
url_paths['url20231111203216'] = '/employee/file-upload'


@app.route(url_paths['url20231111203216'])
def route20231111203226():
    return '''
    <!doctype html>
    <title>직원 파일 업로드 게시판</title>
    <h1>직원 파일 업로드 게시판</h1>
    <!-- __________________________________________________________________________________________________________________________________ 파일 업로드 처리 s -->
    <form name='form-file-upload' action="/employee/file-upload_" method="post" enctype="multipart/form-data">
        <input  type="file" name="file" value="promised202311110318" id="link20231111185433">
        <button type="submit">파일 업로드 처리</button>
    </form>
    <!-- __________________________________________________________________________________________________________________________________ 파일 업로드 처리 e -->
    '''


from werkzeug.utils import secure_filename

url_paths['url20231111185216'] = '/employee/file-upload_'


@app.route(url_paths['url20231111185216'], methods=['GET', 'POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and check_allowed_file_or_not(file.filename):
        filename = secure_filename(file.filename)
        app.logger.debug(file)
        file.save(secure_filename(file.filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        app.logger.debug('파일 업로드 시도되었습니다.debugging20231111190921')
        return redirect(url_paths['url20231111161629'])
        app.logger.debug(os.path.join(app.root_path, app.config['UPLOAD_FOLDER']))
        app.logger.debug(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        time.sleep(random.uniform(3, 5))
        return redirect(request.url)
    return '''
    <!doctype html>
    <title>업로드 실패 왜 안되는지 이유를 찾지 못했다.</title>
    <h1>업로드 실패 왜 안되는지 이유를 찾지 못했다.</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


# params = {
#     "param1": id,
#     "param2": password,
#     "param3": name
# }
# res = requests.post("http://127.0.0.1:9090/handle_post", data=json.dumps(params))


'''
퍼피갤러리 쇼핑몰
'''
# url_paths['url20231111124533'] = '/home/main'
# @app.route(url_paths['url20231111124533'])
# def route20231111124911():
#     name = 'Jung Hoon Park'
#     content =''
#     content+=f'''
#         <!doctype html>
#         <title>퍼피갤러리</title>
#         <h1>{name} 님 안녕하세요! 퍼피갤러리입니다</h1>
#     '''
#     return render_template('/home/main.html', name=name, context='????')


# <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>


'''
이 페이지는 아직 정의하지 않았습니다
'''
url_paths['url202311100025'] = '/test-native-query'


@app.route(url_paths['url202311100025'])
def test_native_query_and_render():
    # print(" __________________________________________________________________________________________________________________________________ native_query to dictionary s[명시적이기 때문에 베스트 같다]")
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
    # print(" __________________________________________________________________________________________________________________________________ native_query to dictionary e")

    # print(" __________________________________________________________________________________________________________________________________ native_query to dictionary as update sql s")
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
    # print(" __________________________________________________________________________________________________________________________________ native_query to dictionary as update sql e")
    # print(" __________________________________________________________________________________________________________________________________ native_query to json s")
    # print(" __________________________________________________________________________________________________________________________________ native_query to json e")
    print(" __________________________________________________________________________________________________________________________________ query based on ORM insert sql s")
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
    session.add(REQUEST_TB(CUSTOMER_NAME="_박_정_훈_y_", MASSAGE="주문서변경요청", DATE_REQUESTED=get_time_as_style("0"), USE_YN="Y"))
    session.commit()
    session.close()
    print(" __________________________________________________________________________________________________________________________________ query based on ORM insert sql e")
    print(" __________________________________________________________________________________________________________________________________ query based on ORM select sql with like searching s")

    class REQUEST_TB(Base):
        __tablename__ = "REQUEST_TB"
        ID_REQUEST = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
        CUSTOMER_NAME = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
        MASSAGE = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
        DATE_REQUESTED = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
        USE_YN = sqlalchemy.Column(sqlalchemy.VARCHAR(length=2))

    print(
        " __________________________________________________________________________________________________________________________________ query based on ORM select sql with like searching e")

    return ''


'''
이 페이지는 아직 정의하지 않았습니다
'''
url_paths['url202311100032'] = '/get/board/<id>'


@app.route(url_paths['url202311100032'])
def getId(id):
    print(id)
    return str(id)


'''
이 페이지는 아직 정의하지 않았습니다
'''
url_paths['url202311100034'] = '/test-singlepage-data-request-via-get-post-request'


@app.route(url_paths['url202311100034'], methods=['GET', 'POST'])
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
        ''' % (url_paths['url202311100034'])
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
url_paths['url202311100033'] = '/SINGLEPAGE_ROUTING1'


@app.route(url_paths['url202311100033'], methods=['GET', 'POST'])
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
        ''' % (url_paths['url202311100033'])

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


# __________________________________________________________________________________________________________________________________ controller e


def main():
    # :: development mode
    # app.run(host=config_web['host'], debug=True, port=config_web['port'])
    # 왜 인지는 모르겠으나 debug=True 하면 os.system($url) 꼴로 작성한 코드가 두번 실행이 되었다.

    # :: pruduction mode
    app.run(host=config_web['host'],  port=config_web['port'])
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    # ssl_context.load_cert_chain(certfile='newcert.pem', keyfile='newkey.pem', password='secret')
    # app.run(host="0.0.0.0", port=4443, ssl_context=ssl_context)


def open_routing_test_automatically():
    # :: url 라우팅 테스트
    # os.system('explorer "http://' + config_web['host'] + ':' + str(config_web['port']) + '' +  url_paths['url202311100030'] ) # url_paths['url202311100030'] = '/urls-routing-test'
    # os.system('explorer "http://' + config_web['host'] + ':' + str(config_web['port']) + '' +  url_paths['url202311110140'] ) # url_paths['url202311110140'] = '/temp'   # 개발자 페이지
    os.system('explorer "http://' + config_web['host'] + ':' + str(config_web['port']) + '' + url_paths['url202311100026'])  # 스타팅 페이지
    # os.system('explorer "http://' + config_web['host'] + ':' + str(config_web['port']) + '' +  url_paths['url202311111422'] ) # 직원 페이지
    # os.system('explorer "http://' + config_web['host'] + ':' + str(config_web['port']) + '' +  url_paths['url202311100027'] ) # 템플릿 실험
    # os.system('explorer "http://'+web['host']+':'+str(web['port'])+''+url_paths['url202311100032'].replace("<id>",str(int(random.random()*100))))

    # :: urls routing map
    # 추후 코드내에서 추출하기 용이하도록 코드작성규칙을 세워 작성.


if __name__ == '__main__':  # 이 파이썬 코드는 뭐냐? 
    app.logger.debug('서버가 디버깅 모드로 시작됩니다.')
    open_routing_test_automatically()
    try:
        main()
    except:
        print(f'''서버 실행 중 예외가 발생했습니다.''')

        # :: 세션 내 모든 값 삭제
        session.clear()
        print(f'''세션 내 모든 값을 삭제하였습니다.''')

    # 야호! 이제 플라스크로 간단한 웹서버를 만들어 직원용 근태관리 서비스를 제공할 수 있다.
# DB 서버 호스팅 : 알아봐야 하는디...   "회사 PC" or "DB 서버 호스팅 업체"
# 웹서버 호스팅


print(" __________________________________________________________________________________________________________________________________  e")
print(" __________________________________________________________________________________________________________________________________  ending log s")
time_e = time.time()
print(f'''서버 종료 시각            : {get_time_as_style('0')}''')
print(f'''서버 라이프 사이클 실행시간 : {time_e - time_s}''')
print(" __________________________________________________________________________________________________________________________________  ending log e")
