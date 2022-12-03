CREATE TRIGGER `UPDATE_SC`
AFTER
UPDATE ON SC FOR EACH ROW BEGIN
UPDATE Student
SET Scholarship = '是'
WHERE Student.Sno = NEW.Sno
    AND NEW.Grade >= 95;
UPDATE Student
SET Scholarship = '否'
WHERE Student.Sno = NEW.Sno
    AND NEW.Grade < 95
    AND NOT EXISTS (
        SELECT *
        FROM SC
        WHERE SC.Sno = NEW.Sno
            AND SC.Grade >= 95
    );
END;
-- 测试触发器效果
UPDATE SC
SET Grade = 98
WHERE Sno = 200215122;
