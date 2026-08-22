// LeetCode 1369 - Get the Second Most Recent Activity
// https://leetcode.com/problems/get-the-second-most-recent-activity/

const char* QUERY =
    "\n"
    "SELECT username, activity, startDate, endDate\n"
    "FROM (\n"
    "  SELECT *, ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) rn,\n"
    "            COUNT(*) OVER (PARTITION BY username) cnt\n"
    "  FROM UserActivity\n"
    ") x\n"
    "WHERE rn = CASE WHEN cnt = 1 THEN 1 ELSE 2 END\n";
