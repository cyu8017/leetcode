// LeetCode 1204 - Last Person to Fit in the Bus
// https://leetcode.com/problems/last-person-to-fit-in-the-bus/

public class Solution {
    public const string QUERY = @"
SELECT person_name
FROM (
    SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
) q
WHERE total_weight <= 1000
ORDER BY turn DESC
LIMIT 1
";
}
