// LeetCode 2230 - The Users That Are Eligible for Discount
// https://leetcode.com/problems/the-users-that-are-eligible-for-discount/

public class Solution {
    public const string QUERY = @"
CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
  SELECT DISTINCT user_id
  FROM Purchases
  WHERE time_stamp BETWEEN startDate AND endDate
    AND amount >= minAmount
  ORDER BY user_id;
END
";
}
