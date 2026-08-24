// LeetCode 2199 - Finding The Topic Of Each Post
// https://leetcode.com/problems/finding-the-topic-of-each-post/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    post_id,\n" +
            "    IFNULL(GROUP_CONCAT(DISTINCT topic_id), 'Ambiguous!') AS topic\n" +
            "FROM\n" +
            "    Posts\n" +
            "    LEFT JOIN Keywords ON INSTR(CONCAT(' ', content, ' '), CONCAT(' ', word, ' ')) > 0\n" +
            "GROUP BY post_id"
    }
}
