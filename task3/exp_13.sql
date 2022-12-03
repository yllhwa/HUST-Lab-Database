CREATE PROCEDURE GradeBySno (IN Sno Int) BEGIN
SELECT Sname,
    Grade
FROM SC,
    Student
WHERE SC.Sno = Student.Sno
    AND SC.Sno = Sno;
END;
call GradeBySno(200215121);