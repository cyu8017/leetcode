// LeetCode 1853 - Convert Date Format
// https://leetcode.com/problems/convert-date-format/

object Solution {
  final val QUERY: String = """SELECT DATE_FORMAT(day, '%W, %M %e, %Y') AS day
FROM Days
"""
}
