// LeetCode 3871 - Count Commas In Range Ii
// https://leetcode.com/problems/count-commas-in-range-ii/

class Solution {
    fun countCommas(n: Long): Long {
        var ans = 0
        run {
            var x = 1000
            while (x <= n) {
                ans += n - x + 1
                x *= 1000
            }
        }
        return ans
    }
}
