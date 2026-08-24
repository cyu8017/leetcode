// LeetCode 2687 - Bikes Last Time Used
// https:// leetcode.com/problems/bikes-last-time-used/

object Solution {
  final val QUERY: String = """SELECT
    bike_number,
    MAX(end_time) AS end_time
FROM Bikes
GROUP BY bike_number
ORDER BY end_time DESC
"""
}
