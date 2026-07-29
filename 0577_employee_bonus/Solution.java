// LeetCode 0577 - Employee Bonus
// https://leetcode.com/problems/employee-bonus/

class Solution {
    public static final String QUERY = """
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL
""";
}
