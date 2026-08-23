// LeetCode 1148 - Article Views I
// https://leetcode.com/problems/article-views-i/

public class Solution {
    public const string QUERY = @"
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id
";
}
