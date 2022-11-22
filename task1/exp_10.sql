SELECT
	Sdept,
	AVG( Sage ) 
FROM
	Student 
GROUP BY
	Sdept;