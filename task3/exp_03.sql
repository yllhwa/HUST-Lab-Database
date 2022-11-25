CREATE VIEW IS_View AS
SELECT DISTINCT Student.*
FROM Student,
    SC
WHERE Student.Sno = SC.Sno
    AND SC.Grade > 80;