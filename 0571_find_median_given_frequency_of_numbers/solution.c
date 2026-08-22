// LeetCode 0571 - Find Median Given Frequency of Numbers
// https://leetcode.com/problems/find-median-given-frequency-of-numbers/

const char* QUERY =
    "\n"
    "WITH stats AS (\n"
    "    SELECT\n"
    "        num,\n"
    "        frequency,\n"
    "        SUM(frequency) OVER (ORDER BY num) AS prefix,\n"
    "        SUM(frequency) OVER () AS total\n"
    "    FROM Numbers\n"
    ")\n"
    "SELECT ROUND(AVG(num), 1) AS median\n"
    "FROM stats\n"
    "WHERE prefix >= FLOOR((total + 1) / 2)\n"
    "  AND prefix - frequency < CEIL((total + 1) / 2.0)\n";
