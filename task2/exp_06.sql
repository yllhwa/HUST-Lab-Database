SELECT Sno,
    Sname,
    Sage
FROM Student
WHERE Ssex = '女'
    AND Sage < (
        SELECT MIN(Sage)
        FROM Student
        WHERE Ssex = '男'
    );