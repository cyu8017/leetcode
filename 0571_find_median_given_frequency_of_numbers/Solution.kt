// LeetCode 0571 - Find Median Given Frequency Of Numbers
// https://leetcode.com/problems/find-median-given-frequency-of-numbers/

class Solution {
    companion object {
        const val QUERY = "WITH stats AS (\n" +
            "    SELECT\n" +
            "        num,\n" +
            "        frequency,\n" +
            "        SUM(frequency) OVER (ORDER BY num) AS prefix,\n" +
            "        SUM(frequency) OVER () AS total\n" +
            "    FROM Numbers\n" +
            ")\n" +
            "SELECT ROUND(AVG(num), 1) AS median\n" +
            "FROM stats\n" +
            "WHERE prefix >= FLOOR((total + 1) / 2)\n" +
            "  AND prefix - frequency < CEIL((total + 1) / 2.0)"
    }
}
