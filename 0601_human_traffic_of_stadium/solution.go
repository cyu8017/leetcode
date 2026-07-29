// LeetCode 0601 - Human Traffic Of Stadium
// https://leetcode.com/problems/human-traffic-of-stadium/

const QUERY = `
WITH busy AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
valid_groups AS (
    SELECT grp
    FROM busy
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT id, visit_date, people
FROM busy
WHERE grp IN (SELECT grp FROM valid_groups)
ORDER BY visit_date
`
