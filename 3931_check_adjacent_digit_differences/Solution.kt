// LeetCode 3931 - Check Adjacent Digit Differences
// https://leetcode.com/problems/check-adjacent-digit-differences/

class Solution {
    fun isAdjacentDiffAtMostTwo(s: String): Boolean {
        for (i in 1 until s.length) {
            if (kotlin.math.abs(s[i - 1] - s[i]) > 2) return false
        }
        return true
    }
}
