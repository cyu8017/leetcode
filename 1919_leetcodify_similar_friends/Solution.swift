// LeetCode 1919 - Leetcodify Similar Friends
// https://leetcode.com/problems/leetcodify-similar-friends/

let QUERY = """
WITH listens AS (
  SELECT DISTINCT user_id, song_id, day
  FROM Listens
),
shared AS (
  SELECT
    LEAST(a.user_id, b.user_id) AS user1_id,
    GREATEST(a.user_id, b.user_id) AS user2_id
  FROM listens a
  JOIN listens b
    ON a.day = b.day
   AND a.song_id = b.song_id
   AND a.user_id < b.user_id
  GROUP BY a.user_id, b.user_id, a.day
  HAVING COUNT(*) >= 3
)
SELECT DISTINCT s.user1_id, s.user2_id
FROM shared s
JOIN Friendship f
  ON f.user1_id = s.user1_id
 AND f.user2_id = s.user2_id
"""
