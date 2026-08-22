// LeetCode 1113 - Reported Posts
// https://leetcode.com/problems/reported-posts/

const char* QUERY =
    "\n"
    "SELECT extra AS report_reason, COUNT(DISTINCT post_id) AS report_count\n"
    "FROM Actions\n"
    "WHERE action = 'report'\n"
    "  AND action_date = '2019-07-04'\n"
    "GROUP BY extra\n";
