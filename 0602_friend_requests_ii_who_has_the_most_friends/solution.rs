// LeetCode 0602 - Friend Requests II: Who Has the Most Friends
// https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/

const QUERY: &str = r#"
SELECT id, COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) friends
GROUP BY id
ORDER BY num DESC
LIMIT 1
"#;
