-- 解法1
SELECT Sno,
    Sname,
    Sage
FROM Student
WHERE Sage IN (
        SELECT Sage
        FROM Student
        WHERE Sname = '张立'
    );
-- 解法2
SELECT Sno,
    Sname,
    Sage
FROM Student
WHERE Sage = (
        SELECT Sage
        FROM Student
        WHERE Sname = '张立'
    );
-- 	解法3
SELECT S1.Sno,
    S1.Sname,
    S1.Sage
FROM Student S1,
    Student S2
WHERE S1.Sage = S2.Sage
    AND S2.Sname = '张立';
-- 	解法4
SELECT Sno,
    Sname,
    Sage
FROM Student S1
WHERE EXISTS (
        SELECT *
        FROM Student S2
        WHERE S2.Sage = S1.Sage
            AND S2.Sname = '张立'
    );