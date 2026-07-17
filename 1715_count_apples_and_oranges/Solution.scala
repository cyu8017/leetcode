// LeetCode 1715 - Count Apples and Oranges
// https://leetcode.com/problems/count-apples-and-oranges/

object Solution {
  final val QUERY: String = """SELECT SUM(apple_count) AS apple_count, SUM(orange_count) AS orange_count
FROM (
    SELECT apple_count, orange_count FROM Boxes
    UNION ALL
    SELECT apple_count, orange_count
    FROM Chests
    WHERE chest_id IN (SELECT chest_id FROM Boxes WHERE chest_id IS NOT NULL)
) AS counts;
"""
}
