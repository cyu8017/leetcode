// LeetCode 1225 - Report Contiguous Dates
// https://leetcode.com/problems/report-contiguous-dates/

export const QUERY = `WITH dates AS (
    SELECT fail_date AS day, 'failed' AS period_state FROM Failed
    UNION ALL
    SELECT success_date, 'succeeded' FROM Succeeded
), grouped AS (
    SELECT day, period_state,
           DATE_SUB(day, INTERVAL ROW_NUMBER() OVER (PARTITION BY period_state ORDER BY day) DAY) AS grp
    FROM dates
    WHERE day BETWEEN '2019-01-01' AND '2019-12-31'
)
SELECT period_state, MIN(day) AS start_date, MAX(day) AS end_date
FROM grouped
GROUP BY period_state, grp
ORDER BY start_date`;
