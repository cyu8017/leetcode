# LeetCode 0627 - Swap Sex of Employees
# https://leetcode.com/problems/swap-sex-of-employees/

QUERY = """
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END
"""
