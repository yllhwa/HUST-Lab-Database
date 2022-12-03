-- 给SC表添加完整性约束，保证Grade在0-100之间
ALTER TABLE SC
ADD CONSTRAINT `Grade`
CHECK (Grade >= 0 AND Grade <= 100);
-- 测试
UPDATE SC
SET Grade = 120
WHERE Sno = 200215122;