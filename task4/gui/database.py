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
