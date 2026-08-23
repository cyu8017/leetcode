// LeetCode 1853 - Convert Date Format
// https://leetcode.com/problems/convert-date-format/

const char* QUERY = R"SQL(
SELECT DATE_FORMAT(day, '%W, %M %e, %Y') AS day
FROM Days
)SQL";
