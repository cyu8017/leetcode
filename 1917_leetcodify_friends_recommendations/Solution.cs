// LeetCode 1917 - Leetcodify Friends Recommendations
// https://leetcode.com/problems/leetcodify-friends-recommendations/

public class Solution {
    public const string QUERY = @"
WITH listens AS (
  SELECT DISTINCT user_id, song_id, day
  FROM Listens
),
shared AS (
  SELECT
    a.user_id AS user_id,
    b.user_id AS recommended_id
  FROM listens a
  JOIN listens b
    ON a.day = b.day
   AND a.song_id = b.song_id
   AND a.user_id <> b.user_id
  GROUP BY a.user_id, b.user_id, a.day
  HAVING COUNT(*) >= 3
)
SELECT DISTINCT s.user_id, s.recommended_id
FROM shared s
LEFT JOIN Friendship f1
  ON f1.user1_id = LEAST(s.user_id, s.recommended_id)
 AND f1.user2_id = GREATEST(s.user_id, s.recommended_id)
WHERE f1.user1_id IS NULL
";
}
