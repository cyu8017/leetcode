// LeetCode 1126 - Active Businesses
// https://leetcode.com/problems/active-businesses/

export const QUERY = `WITH avg_occ AS (
    SELECT event_type, AVG(occurrences) AS avg_occ
    FROM Events
    GROUP BY event_type
)
SELECT DISTINCT e.business_id
FROM Events e
JOIN avg_occ a ON e.event_type = a.event_type
GROUP BY e.business_id
HAVING SUM(e.occurrences > a.avg_occ) > 1`;
