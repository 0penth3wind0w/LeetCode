/*
    2018/08/07
    Not Boring Movies: https://leetcode.com/problems/not-boring-movies/description/
*/

SELECT * FROM cinema WHERE mod(id,2)=1 AND description!='boring' ORDER BY rating DESC;
