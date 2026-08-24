// LeetCode 0571 - Find Median Given Frequency of Numbers
// https://leetcode.com/problems/find-median-given-frequency-of-numbers/

object Solution {
  final val QUERY: String = """WITH stats AS (
    SELECT
        num,
        frequency,
        SUM(frequency) OVER (ORDER BY num) AS prefix,
        SUM(frequency) OVER () AS total
    FROM Numbers
)
SELECT ROUND(AVG(num), 1) AS median
FROM stats
WHERE prefix >= FLOOR((total + 1) / 2)
  AND prefix - frequency < CEIL((total + 1) / 2.0)
"""
}
