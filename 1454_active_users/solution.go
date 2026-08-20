// LeetCode 1454 - Active Users
// https://leetcode.com/problems/active-users/

const QUERY = `
SELECT DISTINCT a.id, a.name
FROM Accounts a
JOIN (
    SELECT id, DATE_SUB(login_date, INTERVAL DENSE_RANK() OVER
        (PARTITION BY id ORDER BY login_date) DAY) AS grp
    FROM (SELECT DISTINCT id, login_date FROM Logins) d
) x ON x.id = a.id
GROUP BY a.id, a.name, x.grp
HAVING COUNT(*) >= 5
`
