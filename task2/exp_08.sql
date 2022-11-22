UPDATE Student
SET Sage = Sage + 2
WHERE Sno IN (
        SELECT DISTINCT Sno
        FROM SC
        WHERE Grade BETWEEN 80 AND 89
    );
SELECT Sage
FROM Student
WHERE Sno IN (
        SELECT DISTINCT Sno
        FROM SC
        WHERE Grade BETWEEN 80 AND 89
    );