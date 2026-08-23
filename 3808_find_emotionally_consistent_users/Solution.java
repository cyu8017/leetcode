// LeetCode 3808 - Find Emotionally Consistent Users
// https://leetcode.com/problems/find-emotionally-consistent-users/

class Solution {
    public static final String QUERY = """
WITH
    t AS (
        SELECT
            user_id,
            reaction,
            COUNT(1) cnt
        FROM reactions
        GROUP BY 1, 2
    ),
    s AS (
        SELECT
            user_id,
            MAX(cnt) mx_cnt,
            ROUND(MAX(cnt) / SUM(cnt), 2) reaction_ratio
        FROM t
        GROUP BY 1
        HAVING reaction_ratio >= 0.60 AND SUM(cnt) >= 5
    )
SELECT user_id, reaction dominant_reaction, reaction_ratio
FROM
    s
    JOIN t USING (user_id)
WHERE cnt = mx_cnt
ORDER BY 3 DESC, 1;
""";
}
