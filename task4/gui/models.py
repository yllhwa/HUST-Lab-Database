from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Student表
# CREATE TABLE Student (
# 	Sno CHAR ( 9 ) PRIMARY KEY,
# 	Sname CHAR ( 20 ) UNIQUE,
# 	Ssex CHAR ( 2 ),
# 	Sage SMALLINT,
# 	Sdept CHAR ( 20 ),
# 	Scholarship char ( 2 )
# );
# /*表Student的主码为Sno，属性列Sname取唯一值*/


class Student(db.Model):
    __tablename__ = 'Student'
    Sno = db.Column(db.String(9), primary_key=True)
    Sname = db.Column(db.String(20), unique=True)
    Ssex = db.Column(db.String(2))
    Sage = db.Column(db.SmallInteger)
    Sdept = db.Column(db.String(20))
    Scholarship = db.Column(db.String(2))

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

# Course表
# CREATE TABLE Course (
# 	Cno CHAR ( 4 ) PRIMARY KEY,
# 	Cname CHAR ( 40 ),
# 	Cpno CHAR ( 4 ),
# 	Ccredit SMALLINT,
# 	FOREIGN KEY ( Cpno ) REFERENCES Course ( Cno )
# );
# /*表Course的主码为Cno，属性列Cpno(先修课)为外码，被参照表为Course，被参照列是Cno*/


class Course(db.Model):
    __tablename__ = 'Course'
    Cno = db.Column(db.String(4), primary_key=True)
    Cname = db.Column(db.String(40))
    Cpno = db.Column(db.String(4), db.ForeignKey('Course.Cno'))
    Ccredit = db.Column(db.SmallInteger)

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

# SC表
# CREATE TABLE SC (
# 	Sno CHAR ( 9 ),
# 	Cno CHAR ( 4 ),
# 	Grade SMALLINT,
# 	PRIMARY KEY ( Sno, Cno ),
# 	FOREIGN KEY ( Sno ) REFERENCES Student ( Sno ),
# 	FOREIGN KEY ( Cno ) REFERENCES Course ( Cno )
# );
# /*表SC的主码为(Sno, Cno), Sno和Cno均为外码，被参照表分别为Student和Course，被参照列分别为Student.Sno和Course.Cno*/


class SC(db.Model):
    __tablename__ = 'SC'
    Sno = db.Column(db.String(9), db.ForeignKey(
        'Student.Sno'), primary_key=True)
    Cno = db.Column(db.String(4), db.ForeignKey(
        'Course.Cno'), primary_key=True)
    Grade = db.Column(db.SmallInteger)

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