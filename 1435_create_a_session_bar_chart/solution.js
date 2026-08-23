// LeetCode 1435 - Create A Session Bar Chart
// https://leetcode.com/problems/create-a-session-bar-chart/

var QUERY = `WITH numbered AS (
    SELECT id, login_date,
           DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER
                    (PARTITION BY id ORDER BY login_date) DAY) AS grp
    FROM (SELECT DISTINCT id, login_date FROM Logins) d
),
active AS (
    SELECT id FROM numbered GROUP BY id, grp HAVING COUNT(*) >= 5
)
SELECT DISTINCT a.id, a.name
FROM Accounts a JOIN active x ON x.id = a.id
ORDER BY a.id`;

module.exports = { QUERY };
