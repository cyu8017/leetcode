// LeetCode 0627 - Swap Sex Of Employees
// https://leetcode.com/problems/swap-sex-of-employees/

class Solution {
    companion object {
        const val QUERY = "UPDATE Salary\n" +
            "SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END"
    }
}
