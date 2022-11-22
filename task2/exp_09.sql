INSERT INTO Course (Cno, Cname)
VALUES (8, 'C语言'),
    (9, '人工智能');
SELECT Cno,
    Cname
FROM Course
WHERE Cname IN ('C语言', '人工智能')