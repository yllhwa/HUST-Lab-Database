CREATE PROCEDURE CS_Grade () BEGIN
SELECT AVG(Grade),
    MAX(Grade)
FROM SC,
    Student
WHERE SC.Sno = Student.Sno
    AND Sdept = 'CS';
END;
CALL CS_Grade();