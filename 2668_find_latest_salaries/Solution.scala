// LeetCode 2668 - Find Latest Salaries
// https:// leetcode.com/problems/find-latest-salaries/

object Solution {
  final val QUERY: String = """SELECT emp_id, firstname, lastname, salary, department_id
FROM Salary
WHERE (emp_id, salary) IN (
    SELECT emp_id, MAX(salary)
    FROM Salary
    GROUP BY emp_id
)
ORDER BY emp_id
"""
}
