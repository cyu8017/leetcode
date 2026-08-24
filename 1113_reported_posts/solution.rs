// LeetCode 1113 - Reported Posts
// https://leetcode.com/problems/reported-posts/

const QUERY: &str = r#"
SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE action = 'report'
  AND action_date = '2019-07-04'
GROUP BY extra
"#;
