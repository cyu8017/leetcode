// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

class Solution {
    fun numberOfEmployeesWhoMetTarget(hours: IntArray, target: Int): Int {
        var ans = 0
        for (h in hours) { if (h >= target) ans++ }
        return ans
    }
}
