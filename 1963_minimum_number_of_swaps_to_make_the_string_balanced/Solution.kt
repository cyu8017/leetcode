// LeetCode 1963
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

class Solution {
    fun minSwaps(s: String): Int {
        var bal = 0
        var mx = 0
        for (ch in s) {
            if (ch == '[') bal++ else bal--
            mx = minOf(mx, bal)
        }
        return (-mx + 1) / 2
    }
}
