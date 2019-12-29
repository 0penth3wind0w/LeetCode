/*
    2018/08/09
    Classes More Than 5 Students: https://leetcode.com/problems/classes-more-than-5-students/description/
*/

SELECT class FROM (SELECT DISTINCT(student), class FROM courses) AS mid GROUP BY class HAVING count(*)>=5;
