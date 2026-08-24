// LeetCode 2010 - The Number Of Seniors And Juniors To Join The Company Ii
// https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company-ii/

let QUERY = """
WITH
    s AS (
        SELECT
            employee_id,
            SUM(salary) OVER (ORDER BY salary) AS cur
        FROM Candidates
        WHERE experience = 'Senior'
    ),
    j AS (
        SELECT
            employee_id,
            IFNULL(
                (SELECT
                    MAX(cur)
                FROM s
                WHERE cur <= 70000),
                0
            ) + SUM(salary) OVER (ORDER BY salary) AS cur
        FROM Candidates
        WHERE experience = 'Junior'
    )
SELECT
    employee_id
FROM s
WHERE cur <= 70000
UNION
SELECT
    employee_id
FROM j
WHERE cur <= 70000
"""
