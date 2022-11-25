SELECT DISTINCT IS_View.*
FROM IS_View,
    SC
WHERE IS_View.Sno = SC.Sno
    AND SC.Grade > 80;