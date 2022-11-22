SELECT Course.Cno,
    Cname,
    Sno,
    Grade
FROM Course
    LEFT OUTER JOIN SC ON (Course.Cno = SC.Cno);