// LeetCode 0627 - Swap Sex of Employees
// https://leetcode.com/problems/swap-sex-of-employees/

object Solution {
  final val QUERY: String = """UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END
"""
}
