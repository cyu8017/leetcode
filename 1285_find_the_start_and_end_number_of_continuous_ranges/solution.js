// LeetCode 1285 - Find The Start And End Number Of Continuous Ranges
// https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/

var QUERY = `SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id
FROM (
    SELECT log_id, log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp
    FROM Logs
) numbered
GROUP BY grp
ORDER BY start_id`;

module.exports = { QUERY };
