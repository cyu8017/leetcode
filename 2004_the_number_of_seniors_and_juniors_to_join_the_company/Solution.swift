// LeetCode 2004 - The Number Of Seniors And Juniors To Join The Company
// https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/

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
    'Senior' AS experience,
    COUNT(employee_id) AS accepted_candidates
FROM s
WHERE cur <= 70000
UNION ALL
SELECT
    'Junior' AS experience,
    COUNT(employee_id) AS accepted_candidates
FROM j
WHERE cur <= 70000
"""
