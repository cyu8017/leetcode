// LeetCode 0627 - Swap Sex of Employees
// https://leetcode.com/problems/swap-sex-of-employees/

public class Solution {
    public const string QUERY = @"
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END
";
}
