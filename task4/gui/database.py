from models import Student, Course, SC
from models import db


def getStudentCount():
    return Student.query.count()


def getCourseCount():
    return Course.query.count()


def getSCCount():
    return SC.query.count()


def getStudents(page, size):
    return [i.to_dict() for i in Student.query.paginate(page=page, per_page=size, error_out=False).items]


def getCourses(page, size):
    return [i.to_dict() for i in Course.query.paginate(page=page, per_page=size, error_out=False).items]


def getSCs(page, size):
    return [i.to_dict() for i in SC.query.paginate(page=page, per_page=size, error_out=False).items]


def addStudent(data):
    student = Student(**data)
    db.session.add(student)
    db.session.commit()


def updateStudent(data):
    db.session.query(Student).filter(Student.Sno == data['Sno']).update(data)
    db.session.commit()


def deleteStudent(data):
    db.session.query(Student).filter(Student.Sno == data['Sno']).delete()
    db.session.commit()


def addCourse(data):
    course = Course(**data)
    db.session.add(course)
    db.session.commit()


def updateCourse(data):
    db.session.query(Course).filter(Course.Cno == data['Cno']).update(data)
    db.session.commit()


def deleteCourse(data):
    db.session.query(Course).filter(Course.Cno == data['Cno']).delete()
    db.session.commit()


def addSC(data):
    sc = SC(**data)
    db.session.add(sc)
    db.session.commit()


def updateSC(data):
    db.session.query(SC).filter(
        SC.Sno == data['Sno'], SC.Cno == data['Cno']).update(data)
    db.session.commit()


def deleteSC(data):
    db.session.query(SC).filter(
        SC.Sno == data['Sno'], SC.Cno == data['Cno']).delete()
    db.session.commit()


def getStat(dept):
    # 统计系中学生的平均成绩
    # SELECT AVG(Grade) FROM Student, SC WHERE Student.Sno=SC.Sno AND Student.Sdept='CS'
    average_grade = db.session.query(db.func.avg(SC.Grade)).join(
        Student, Student.Sno == SC.Sno).filter(Student.Sdept == dept).scalar()

    # 统计系中最好成绩
    max_grade = db.session.query(db.func.max(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept).scalar()
    min_grade = db.session.query(db.func.min(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept).scalar()
    # 计算优秀率(>=80为优秀)
    # SELECT COUNT(*) FROM Student, SC WHERE Student.Sno=SC.Sno AND Student.Sdept='CS' AND SC.Grade>=80
    excellent = db.session.query(db.func.count(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept, SC.Grade >= 80).scalar()
    all_count = db.session.query(db.func.count(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
        Student.Sdept == dept).scalar()
    excellent_rate = excellent / all_count
    # 不及格人数
    fail_count = db.session.query(db.func.count(SC.Grade)).join(Student, Student.Sno == SC.Sno).filter(
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
    student_detail = db.session.query(
        Student).filter(Student.Sno == Sno).first()
    _student_courses = [i.to_dict()
                        for i in db.session.query(SC).filter(SC.Sno == Sno).all()]
    for i in _student_courses:
        course_detail = db.session.query(
            Course).filter(Course.Cno == i['Cno']).scalar()
        i['Cname'] = course_detail.Cname
        i['Ccredit'] = course_detail.Ccredit
        i.pop('Sno')
    return {
        "detail": student_detail.to_dict() if student_detail is not None else {},
        "courses": _student_courses
    }
