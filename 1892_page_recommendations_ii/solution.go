// LeetCode 1892 - Page Recommendations II
// https://leetcode.com/problems/page-recommendations-ii/

const QUERY = `
SELECT f.user_id, l.page_id, COUNT(*) AS friends_likes
FROM (
    SELECT user1_id AS user_id, user2_id AS friend_id FROM Friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id FROM Friendship
) f
JOIN Likes l ON l.user_id = f.friend_id
LEFT JOIN Likes ul ON ul.user_id = f.user_id AND ul.page_id = l.page_id
WHERE ul.page_id IS NULL
GROUP BY f.user_id, l.page_id
`
