// LeetCode 2199 - Finding The Topic Of Each Post
// https://leetcode.com/problems/finding-the-topic-of-each-post/

export const QUERY = `SELECT
    post_id,
    IFNULL(GROUP_CONCAT(DISTINCT topic_id), 'Ambiguous!') AS topic
FROM
    Posts
    LEFT JOIN Keywords ON INSTR(CONCAT(' ', content, ' '), CONCAT(' ', word, ' ')) > 0
GROUP BY post_id`;
