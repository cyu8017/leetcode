// LeetCode 1853 - Convert Date Format
// https://leetcode.com/problems/convert-date-format/

public class Solution {
    public const string QUERY = @"
SELECT DATE_FORMAT(day, '%W, %M %e, %Y') AS day
FROM Days
";
}
