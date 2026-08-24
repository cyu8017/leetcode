// LeetCode 3793 - Find Users with High Token Usage
// https:// leetcode.com/problems/find-users-with-high-token-usage/

const QUERY: &str = r#"
SELECT
    user_id,
    COUNT(1) AS prompt_count,
    ROUND(AVG(tokens), 2) AS avg_tokens
FROM prompts
GROUP BY user_id
HAVING prompt_count >= 3 AND MAX(tokens) > avg_tokens
ORDER BY avg_tokens DESC, user_id;
"#;
