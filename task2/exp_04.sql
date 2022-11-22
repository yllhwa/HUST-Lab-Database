SELECT SC.Cno,
    Cname
FROM SC,
    Course
WHERE SC.Cno = Course.Cno
    AND SC.Sno = 200215122;