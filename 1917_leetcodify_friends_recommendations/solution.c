// LeetCode 1917 - Leetcodify Friends Recommendations
// https://leetcode.com/problems/leetcodify-friends-recommendations/

const char* QUERY =
    "\n"
    "WITH listens AS (\n"
    "  SELECT DISTINCT user_id, song_id, day\n"
    "  FROM Listens\n"
    "),\n"
    "shared AS (\n"
    "  SELECT\n"
    "    a.user_id AS user_id,\n"
    "    b.user_id AS recommended_id\n"
    "  FROM listens a\n"
    "  JOIN listens b\n"
    "    ON a.day = b.day\n"
    "   AND a.song_id = b.song_id\n"
    "   AND a.user_id <> b.user_id\n"
    "  GROUP BY a.user_id, b.user_id, a.day\n"
    "  HAVING COUNT(*) >= 3\n"
    ")\n"
    "SELECT DISTINCT s.user_id, s.recommended_id\n"
    "FROM shared s\n"
    "LEFT JOIN Friendship f1\n"
    "  ON f1.user1_id = LEAST(s.user_id, s.recommended_id)\n"
    " AND f1.user2_id = GREATEST(s.user_id, s.recommended_id)\n"
    "WHERE f1.user1_id IS NULL\n";
