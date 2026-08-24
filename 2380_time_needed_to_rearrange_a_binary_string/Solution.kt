// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

class Solution {
    fun secondsToRemoveOccurrences(s: String): Int {
        var ans = 0
        var zeros = 0
        for (c in s) {
            if (c == '0') zeros++
            else if (zeros > 0) ans = maxOf(ans + 1, zeros)
        }
        return ans
    }
}
