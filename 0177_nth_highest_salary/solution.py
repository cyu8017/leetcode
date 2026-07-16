# LeetCode 0177 - Nth Highest Salary
# https://leetcode.com/problems/nth-highest-salary/

# Write your MySQL query statement below
QUERY = """
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  RETURN (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET M
  );
END
"""
