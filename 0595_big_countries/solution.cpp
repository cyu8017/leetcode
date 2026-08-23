// LeetCode 0595 - Big Countries
// https://leetcode.com/problems/big-countries/

const char* QUERY = R"SQL(
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000
)SQL";
