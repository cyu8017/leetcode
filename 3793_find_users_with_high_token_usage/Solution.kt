// LeetCode 3793 - Find Users With High Token Usage
// https://leetcode.com/problems/find-users-with-high-token-usage/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    user_id,\n" +
            "    COUNT(1) AS prompt_count,\n" +
            "    ROUND(AVG(tokens), 2) AS avg_tokens\n" +
            "FROM prompts\n" +
            "GROUP BY user_id\n" +
            "HAVING prompt_count >= 3 AND MAX(tokens) > avg_tokens\n" +
            "ORDER BY avg_tokens DESC, user_id;"
    }
}
