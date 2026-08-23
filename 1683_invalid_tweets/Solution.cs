// LeetCode 1683 - Invalid Tweets
// https://leetcode.com/problems/invalid-tweets/

public class Solution {
    public const string QUERY = @"
SELECT tweet_id FROM Tweets WHERE CHAR_LENGTH(content)>15
";
}
