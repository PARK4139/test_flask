config_web = {
    # 'host': '0.0.0.0',   #모든 public ip 허용
    'host': '127.0.0.1',   #localhost ip 만 허용
    # 'port': 80,          #80 은 웹기본포트 로 아무 포트로 들어올 수 있게 하는 포트인가?
    'port': 9090, #  
}
# 443 port는 ssl ?    보안계층인 ssl 거쳐서 연결되는 것 같음. 아마도.
config_db = {
    "maria_db_vertion": '11.1 alpha', # not LTS
    'user': 'root',
    'password': 'ju7987LI&',
    'host': '127.0.0.1',
    'port': 3306, # maria DB default TCP port
    'database': 'schema_employee'
}

db_url = f"mariadb+pymysql://{config_db['user']}:{config_db['password']}@{config_db['host']}:{config_db['port']}/{config_db['database']}?charset=utf8mb4"
# f"{db['host']}:{db['port']}/{db['database']}?charset=utf8"


url_error_pages={
    'default': "http://" + config_web['host'] + ":" + str(config_web['port']) + "/error" ,
    '404': "http://" + config_web['host'] + ":" + str(config_web['port']) + "/error/404.html",
    '500': "http://" + config_web['host'] + ":" + str(config_web['port']) + "/error/500.html",
}

url_paths= dict()


