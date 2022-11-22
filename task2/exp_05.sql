SELECT Sno,
    Cno
FROM SC x
WHERE Grade < (
        SELECT AVG(Grade) - 5
        FROM SC y
        WHERE y.Sno = x.Sno
    )