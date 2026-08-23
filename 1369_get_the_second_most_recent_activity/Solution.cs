// LeetCode 1369 - Get the Second Most Recent Activity
// https://leetcode.com/problems/get-the-second-most-recent-activity/

public class Solution {
    public const string QUERY = @"
SELECT username, activity, startDate, endDate
FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) rn,
            COUNT(*) OVER (PARTITION BY username) cnt
  FROM UserActivity
) x
WHERE rn = CASE WHEN cnt = 1 THEN 1 ELSE 2 END
";
}
