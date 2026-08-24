// LeetCode 1270 - All People Report To The Given Manager
// https://leetcode.com/problems/all-people-report-to-the-given-manager/

object Solution {
  final val QUERY: String = """WITH RECURSIVE reports AS (
    SELECT employee_id
    FROM Employees
    WHERE manager_id = 1 AND employee_id <> 1
    UNION ALL
    SELECT e.employee_id
    FROM Employees e
    JOIN reports r ON e.manager_id = r.employee_id
)
SELECT employee_id
FROM reports
WHERE employee_id <> 1
"""
}
