CREATE TABLE Student (
    Sno CHAR (9) PRIMARY KEY,
    Sname CHAR (20) UNIQUE,
    Ssex CHAR (2),
    Sage SMALLINT,
    Sdept CHAR (20),
    Scholarship char (2)
);
/*表Student的主码为Sno，属性列Sname取唯一值*/
CREATE TABLE Course (
    Cno CHAR (4) PRIMARY KEY,
    Cname CHAR (40),
    Cpno CHAR (4),
    Ccredit SMALLINT,
    FOREIGN KEY (Cpno) REFERENCES Course (Cno)
);
/*表Course的主码为Cno，属性列Cpno(先修课)为外码，被参照表为Course，被参照列是Cno*/
CREATE TABLE SC (
    Sno CHAR (9),
    Cno CHAR (4),
    Grade SMALLINT,
    PRIMARY KEY (Sno, Cno),
    FOREIGN KEY (Sno) REFERENCES Student (Sno),
    FOREIGN KEY (Cno) REFERENCES Course (Cno)
);
/*表SC的主码为(Sno, Cno), Sno和Cno均为外码，被参照表分别为Student和Course，被参照列分别为Student.Sno和Course.Cno*/