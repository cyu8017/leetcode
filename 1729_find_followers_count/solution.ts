// LeetCode 1729 - Find Followers Count
// https://leetcode.com/problems/find-followers-count/

export const QUERY = `SELECT user_id, COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;`;
