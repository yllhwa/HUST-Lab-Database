SELECT
	Sdept,
	AVG( Sage ) 
FROM
	( SELECT Sdept, AVG( Sage ) AS Sage FROM Student GROUP BY Sdept ) 
WHERE
	Sage <= 19 
GROUP BY
	Sdept;