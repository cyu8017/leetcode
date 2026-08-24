// LeetCode 2199 - Finding the Topic of Each Post
// https:// leetcode.com/problems/finding-the-topic-of-each-post/

const QUERY: &str = r#"
SELECT
    post_id,
    IFNULL(GROUP_CONCAT(DISTINCT topic_id), 'Ambiguous!') AS topic
FROM
    Posts
    LEFT JOIN Keywords ON INSTR(CONCAT(' ', content, ' '), CONCAT(' ', word, ' ')) > 0
GROUP BY post_id
"#;
