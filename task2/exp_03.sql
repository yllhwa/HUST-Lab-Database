SELECT Student.Sno,
    Sname
FROM Student,
    SC
WHERE Student.Sno = SC.Sno
    AND SC.Cno = 3
    AND SC.Grade BETWEEN 80 AND 89;