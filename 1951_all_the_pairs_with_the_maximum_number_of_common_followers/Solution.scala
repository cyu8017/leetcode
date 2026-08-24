// LeetCode 1951 - All The Pairs With The Maximum Number Of Common Followers
// https://leetcode.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers/

object Solution {
  final val QUERY: String = """WITH commons AS (
  SELECT r1.user_id AS user1_id,
         r2.user_id AS user2_id,
         COUNT(*) AS cnt
  FROM Relations r1
  JOIN Relations r2
    ON r1.follower_id = r2.follower_id
   AND r1.user_id < r2.user_id
  GROUP BY r1.user_id, r2.user_id
)
SELECT user1_id, user2_id
FROM commons
WHERE cnt = (SELECT MAX(cnt) FROM commons)
"""
}
