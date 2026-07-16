public class Solution {
    public const string QUERY = @"
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1
";
}
