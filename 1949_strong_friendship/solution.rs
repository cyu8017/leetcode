// LeetCode 1949 - Strong Friendship
// https://leetcode.com/problems/strong-friendship/

const QUERY: &str = r#"
WITH F AS (
  SELECT user1_id, user2_id FROM Friendship
  UNION ALL
  SELECT user2_id, user1_id FROM Friendship
)
SELECT a.user1_id, a.user2_id, COUNT(*) AS common_friend
FROM Friendship a
JOIN F b ON a.user1_id = b.user1_id
JOIN F c ON a.user2_id = c.user1_id AND b.user2_id = c.user2_id
GROUP BY a.user1_id, a.user2_id
HAVING COUNT(*) >= 3
"#;
