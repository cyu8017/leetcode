// LeetCode 2837 - Total Traveled Distance
// https://leetcode.com/problems/total-traveled-distance/

export const QUERY = `SELECT u.user_id, u.name, IFNULL(SUM(r.distance), 0) AS`;
