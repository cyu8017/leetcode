// LeetCode 0627 - Swap Sex Of Employees
// https://leetcode.com/problems/swap-sex-of-employees/

class Solution {
    public static final String QUERY = """
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END
""";
}
