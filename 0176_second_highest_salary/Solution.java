// LeetCode 0176 - Second Highest Salary
// https://leetcode.com/problems/second-highest-salary/

class Solution {
    public static final String QUERY = """
SELECT
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary
""";
}
