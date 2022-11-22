SELECT
	Sno,
	Cno,
	Grade 
FROM
	SC 
WHERE
	Grade >= 90 
	OR Grade < 60;