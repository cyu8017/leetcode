// LeetCode 0570 - Managers with at Least 5 Direct Reports
// https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

object Solution {
  final val QUERY: String = """SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)
"""
}
