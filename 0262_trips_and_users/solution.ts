// LeetCode 0262 - Trips and Users
// https://leetcode.com/problems/trips-and-users/

export const QUERY = `SELECT
    Request_at AS Day,
    ROUND(
        SUM(CASE WHEN Status <> 'completed' THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS \`Cancellation Rate\`
FROM Trips
INNER JOIN Users ON Trips.Client_Id = Users.Users_Id AND Users.Role = 'client'
WHERE Users.Banned = 'No'
    AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Request_at
ORDER BY Day`;
