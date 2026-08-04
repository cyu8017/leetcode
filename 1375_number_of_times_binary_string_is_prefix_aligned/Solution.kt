// LeetCode 1375 - Number of Times Binary String Is Prefix-Aligned
// https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/

class Solution {
    fun numTimesAllBlue(flips: IntArray): Int {
        var ans = 0
        var mx = 0
        for (i in flips.indices) {
            mx = maxOf(mx, flips[i])
            if (mx == i + 1) ans++
        }
        return ans
    }
}
