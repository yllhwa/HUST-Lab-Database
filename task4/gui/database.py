# session
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, SmallInteger, String, ForeignKey
from sqlalchemy import create_engine
engine = create_engine("sqlite:///database.db",
                       connect_args={'check_same_thread': False})
Base = declarative_base()
session = scoped_session(sessionmaker(bind=engine))
Base.query = session.query_property()


class Student(Base):
    __tablename__ = 'Student'
    Sno = Column(String(9), primary_key=True)
    Sname = Column(String(20), unique=True)
    Ssex = Column(String(2))
    Sage = Column(SmallInteger)
    Sdept = Column(String(20))
    Scholarship = Column(String(2))

    def __init__(self, Sno, Sname, Ssex, Sage, Sdept, Scholarship):
        self.Sno = Sno
        self.Sname = Sname
        self.Ssex = Ssex
        self.Sage = Sage
        self.Sdept = Sdept
        self.Scholarship = Scholarship

    def __repr__(self):
        return '<Student %r>' % self.Sno

    def to_dict(self):
        return {
            'Sno': self.Sno,
            'Sname': self.Sname,
            'Ssex': self.Ssex,
            'Sage': self.Sage,
            'Sdept': self.Sdept,
            'Scholarship': self.Scholarship
        }


class Course(Base):
    __tablename__ = 'Course'
    Cno = Column(String(4), primary_key=True)
    Cname = Column(String(40))
    Cpno = Column(String(4), ForeignKey('Course.Cno'))
    Ccredit = Column(SmallInteger)

    def __init__(self, Cno, Cname, Cpno, Ccredit):
        self.Cno = Cno
        self.Cname = Cname
        self.Cpno = Cpno
        self.Ccredit = Ccredit

    def __repr__(self):
        return '<Course %r>' % self.Cno

    def to_dict(self):
        return {
            'Cno': self.Cno,
            'Cname': self.Cname,
            'Cpno': self.Cpno,
            'Ccredit': self.Ccredit
        }


class SC(Base):
    __tablename__ = 'SC'
    Sno = Column(String(9), ForeignKey(
        'Student.Sno'), primary_key=True)
    Cno = Column(String(4), ForeignKey(
        'Course.Cno'), primary_key=True)
    Grade = Column(SmallInteger)

    def __init__(self, Sno, Cno, Grade):
        self.Sno = Sno
        self.Cno = Cno
        self.Grade = Grade

    def __repr__(self):
        return '<SC %r %r>' % (self.Sno, self.Cno)

    def to_dict(self):
        return {
            'Sno': self.Sno,
            'Cno': self.Cno,
            'Grade': self.Grade
        }


def getStudentCount():
    return session.query(func.count(Student.Sno)).scalar()


def getCourseCount():
    return session.query(func.count(Course.Cno)).scalar()


def getSCCount():
    return session.query(func.count(SC.Sno)).scalar()


def getStudents(page, size):
    students = session.query(Student).limit(
        size).offset((page - 1) * size).all()
    return [i.to_dict() for i in students]


def getCourses(page, size):
    courses = session.query(Course).limit(
        size).offset((page - 1) * size).all()
    return [i.to_dict() for i in courses]


def getSCs(page, size):
    scs = session.query(SC).limit(
        size).offset((page - 1) * size).all()
    return [i.to_dict() for i in scs]


def addStudent(data):
    student = Student(**data)
    session.add(student)
    session.commit()


def updateStudent(data):
    session.query(Student).filter(Student.Sno == data['Sno']).update(data)
    session.commit()


def deleteStudent(data):
    session.query(Student).filter(Student.Sno == data['Sno']).delete()
    session.commit()


def addCourse(data):
    course = Course(**data)
    session.add(course)
    session.commit()


def updateCourse(data):
    session.query(Course).filter(Course.Cno == data['Cno']).update(data)
    session.commit()


def deleteCourse(data):
    session.query(Course).filter(Course.Cno == data['Cno']).delete()
    session.commit()


def addSC(data):
    sc = SC(**data)
    session.add(sc)
    session.commit()


def updateSC(data):
    session.query(SC).filter(
        SC.Sno == data['Sno'], SC.Cno == data['Cno']).update(data)
    session.commit()


def deleteSC(data):
    session.query(SC).filter(
        SC.Sno == data['Sno'], SC.Cno == data['Cno']).delete()
    session.commit()


def getStat(dept):
    # 统计系中学生的平均成绩
    # SELECT AVG(Grade) FROM Student, SC WHERE Student.Sno=SC.Sno AND Student.Sdept='CS'
    average_grade = session.query(func.avg(SC.Grade)).join(
        Student, Student.Sno == SC.Sno).filter(Student.Sdept == dept).scalar()

    # 统计系中最好成绩
    max_grade = session.query(func.max(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept).scalar()
    min_grade = session.query(func.min(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept).scalar()
    # 计算优秀率(>=80为优秀)
    # SELECT COUNT(*) FROM Student, SC WHERE Student.Sno=SC.Sno AND Student.Sdept='CS' AND SC.Grade>=80
    excellent = session.query(func.count(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept, SC.Grade >= 80).scalar()
    all_count = session.query(func.count(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept).scalar()
    excellent_rate = excellent / all_count
    # 不及格人数
    fail_count = session.query(func.count(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept, SC.Grade < 60).scalar()
    return {
        "average_grade": average_grade if average_grade is not None else 0,
        "max_grade": max_grade if max_grade is not None else 0,
        "min_grade": min_grade if min_grade is not None else 0,
        "excellent_rate": excellent_rate if excellent_rate is not None else 0,
        "fail_count": fail_count if fail_count is not None else 0
    }


def getRank(dept):
    # todo
    pass


def search(Sno):
    # 返回学生详细信息和选课信息
    # SELECT * FROM Student, SC WHERE Student.Sno=SC.Sno AND Student.Sno='S1'
    student_detail = session.query(
        Student).filter(Student.Sno == Sno).first()
    _student_courses = [i.to_dict()
                        for i in session.query(SC).filter(SC.Sno == Sno).all()]
    for i in _student_courses:
        course_detail = session.query(
            Course).filter(Course.Cno == i['Cno']).scalar()
        i['Cname'] = course_detail.Cname
        i['Ccredit'] = course_detail.Ccredit
        i.pop('Sno')
    return {
        "detail": student_detail.to_dict() if student_detail is not None else {},
        "courses": _student_courses
    }
