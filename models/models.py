import sqlalchemy
from sqlalchemy import Integer, Column, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, backref

from config import db_url

engine = sqlalchemy.create_engine(db_url)  # db_url 변경 소지 있음.
Base = declarative_base()
Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


# class REQUEST_TB(Base):
#     __tablename__ = "REQUEST_TB"
#     # __table_args__ = {'mysql_collate': 'utf8_general_ci'}  # encoding 안되면 비슷하게 방법을 알아보자  mysql 용 코드로 보인다.
#     ID_REQUEST = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
#     CUSTOMER_NAME = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
#     MASSAGE = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
#     DATE_REQUESTED = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
#     USE_YN = sqlalchemy.Column(sqlalchemy.VARCHAR(length=2))
#
#     def __init__(self, ID_REQUEST, CUSTOMER_NAME, MASSAGE, DATE_REQUESTED, USE_YN):
#         self.ID_REQUEST = ID_REQUEST
#         self.CUSTOMER_NAME = CUSTOMER_NAME
#         self.MASSAGE = MASSAGE
#         self.DATE_REQUESTED = DATE_REQUESTED
#         self.USE_YN = USE_YN
#
#     def add_new_records(ID_REQUEST, CUSTOMER_NAME, MASSAGE, DATE_REQUESTED, USE_YN):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         new_records = REQUEST_TB(ID_REQUEST=ID_REQUEST, CUSTOMER_NAME=CUSTOMER_NAME, MASSAGE=MASSAGE, DATE_REQUESTED=DATE_REQUESTED, USE_YN=USE_YN)
#         session.add(new_records)
#         session.commit()
#
#     @staticmethod
#     def select_records_all():
#         print("_______________________________________________________________ " + inspect.currentframe().f_code.co_name + " s")
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).all()
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#         print(records_as_str)
#         print("_______________________________________________________________ " + inspect.currentframe().f_code.co_name + " e")
#         return records_as_str
#
#     def select_records_by_id_Request(ID_REQUEST):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         return session.query(REQUEST_TB).filter_by(ID_REQUEST=ID_REQUEST).order_by(REQUEST_TB.ID_REQUEST.desc()).all()
#
#     def select_records_by_id_request(ID_REQUEST):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         return session.query(REQUEST_TB).filter_by_(ID_REQUEST=ID_REQUEST).first()
#
#     # def select_records_by_id_Request(ID_REQUEST, CUSTOMER_NAME):
#     #     return session.query(REQUEST_TB).filter(and_(REQUEST_TB.ID_REQUEST == item['ID_REQUEST'],
#     #                                                  REQUEST_TB.sequence_id == item['sequence_id'])).all()
#
#     def select_records_by_RowNumber(RowNumber):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).get(RowNumber)
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def select_records_by_CUSTOMER_NAME_via_like(CUSTOMER_NAME='_박_정_훈_'):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).filter(REQUEST_TB.CUSTOMER_NAME.like('%' + CUSTOMER_NAME + '%'))
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def select_records_where_CUSTOMER_NAME_is_not_(CUSTOMER_NAME='_박_정_훈_'):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).first(REQUEST_TB.CUSTOMER_NAME != CUSTOMER_NAME)
#         records_as_str = ''
#         for record in records:
#             tmp = '{{delimeter}}' + str(record.ID_REQUEST) + '{{delimeter}}' + record.CUSTOMER_NAME + '{{delimeter}}' + record.MASSAGE + '{{delimeter}}' + record.DATE_REQUESTED + '{{delimeter}}' + record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def select_records_by_Status(isActive):  # ,이건 뭐지?
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).filter_by_(active=isActive)
#         records_as_str = ''
#         for Record in records:
#             tmp = '{{delimeter}}' + str(Record.ID_REQUEST) + '{{delimeter}}' + Record.CUSTOMER_NAME + '{{delimeter}}' + Record.MASSAGE + '{{delimeter}}' + Record.DATE_REQUESTED + '{{delimeter}}' + Record.USE_YN + ' \n'
#             records_as_str += tmp
#             print(records_as_str)
#         return records_as_str
#
#     def update_record_status(ID_REQUEST, isActive):  # isActive 이건 뭐지?  use_yn 개념 같아 보인다.
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         records = session.query(REQUEST_TB).get(ID_REQUEST)
#         records.active = isActive
#         session.commit()
#
#     def update_record_of_MASSAGE_by_ID_REQUEST(ID_REQUEST, MASSAGE):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         session.query(REQUEST_TB).filter(REQUEST_TB.ID_REQUEST == ID_REQUEST).first().MASSAGE = MASSAGE
#         session.commit()
#
#     def delete_records_by_ID_REQUEST(ID_REQUEST):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         session.query(REQUEST_TB).filter(REQUEST_TB.ID_REQUEST == ID_REQUEST).delete()
#         session.commit()
#
#     def delete_records_by_CUSTOMER_NAME(CUSTOMER_NAME='_박_정_훈_'):
#         Session = sqlalchemy.orm.sessionmaker()
#         Session.configure(bind=engine)
#         session = Session()
#         session.query(REQUEST_TB).filter(REQUEST_TB.CUSTOMER_NAME == CUSTOMER_NAME).delete()
#         session.commit()


class Question():
    id = Column(Integer, primary_key=True)
    subject = Column(String(200), nullable=False)
    content = Column(Text(), nullable=False)
    create_date = Column(DateTime(), nullable=False)


class Answer():
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id', ondelete='CASCADE'))
    question = relationship('Question', backref=backref('answer_set'))
    content = Column(Text(), nullable=False)
    create_date = Column(DateTime(), nullable=False)


#  __________________________________________________________________________________________________________________________________ employee_joined_list s

class employee_joined_list(Base):
    __tablename__ = "employee_joined_list"
    # __table_args__ = {'mysql_collate': 'utf8_general_ci'}  # encoding 안되면 비슷하게 방법을 알아보자  mysql 에 적용이 가능한 코드로 보인다.
    id_autoincrement = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    id = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
    e_mail = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
    phone_no = sqlalchemy.Column(sqlalchemy.VARCHAR(length=11))
    address = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
    age = sqlalchemy.Column(sqlalchemy.VARCHAR(length=2))
    pw = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
    date_joined = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
    date_canceled = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))

    def __init__(self,
                 # id_autoincrement,
                 name,
                 id,
                 pw,
                 e_mail,
                 phone_no,
                 address,
                 age,
                 date_joined,
                 date_canceled
                 ):
        # self.id_autoincrement = id_autoincrement
        self.name = name
        self.id = id
        self.pw = pw
        self.e_mail = e_mail
        self.phone_no = phone_no
        self.address = address
        self.age = age
        self.date_joined = date_joined
        self.date_canceled = date_canceled

    def add_new_records(name, id, pw, e_mail, phone_no, address, age, date_joined, date_canceled):
        new_records = employee_joined_list(
            name=name,
            id=id,
            pw=pw,
            e_mail=e_mail,
            phone_no=phone_no,
            address=address,
            age=age,
            date_joined=date_joined,
            date_canceled=date_canceled
        )
        session.add(new_records)
        session.commit()
        session.close()  # 사용 후 닫아야 하는지 이거 맞는지는 모르겠다.실험해보자
        return new_records

    def get_employee_joined(id, pw):
        # :: NATIVE QUERY 사용 방식
        # select_result = f'''SELECT * FROM employee_joined_list where id= {id} and pw= {pw} ORDER BY date_joined LIMIT 2;'''

        # :: ORM 사용 방식
        select_result = session.query(employee_joined_list).filter_by(id=id, pw=pw).limit(2)
        # select_result = session.query(employee_joined_list).filter_by(id=id, pw=pw).first()
        # select_result = session.query(employee_joined_list).filter_by(id=id).order_by(employee_joined_list.id_autoincrement.desc()).all()
        # select_result = session.query(employee_joined_list).filter(employee_joined_list.name.ilike("%_박_정_훈_%").all_())
        return select_result


#  __________________________________________________________________________________________________________________________________ employee_joined_list e
#  __________________________________________________________________________________________________________________________________ employee_commutation_management_tb s

class employee_commutation_management_tb(Base):
    __tablename__ = "employee_commutation_management_tb"
    id_autoincrement = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, autoincrement=True)
    id = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(length=13))
    time_to_go_to_office = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))
    time_to_leave_office = sqlalchemy.Column(sqlalchemy.VARCHAR(length=100))

    def __init__(self, name, id, time_to_go_to_office, time_to_leave_office):
        self.name = name
        self.id = id
        self.time_to_go_to_office = time_to_go_to_office
        self.time_to_leave_office = time_to_leave_office

    def add_new_record(name, id, time_to_go_to_office, time_to_leave_office):
        new_records = employee_commutation_management_tb(name=name, id=id, time_to_go_to_office=time_to_go_to_office, time_to_leave_office=time_to_leave_office)
        session.add(new_records)
        session.commit()
        session.close()  # 사용 후 닫아야 하는지 이거 맞는지는 모르겠다.실험해보자
        return new_records

#  __________________________________________________________________________________________________________________________________ employee_commutation_management_tb e
