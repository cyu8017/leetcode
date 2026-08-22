// LeetCode 0595 - Big Countries
// https://leetcode.com/problems/big-countries/

const char* QUERY =
    "\n"
    "SELECT name, population, area\n"
    "FROM World\n"
    "WHERE area >= 3000000 OR population >= 25000000\n";
