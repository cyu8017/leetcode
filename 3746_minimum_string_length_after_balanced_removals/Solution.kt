// LeetCode 3746 - Minimum String Length After Balanced Removals
// https://leetcode.com/problems/minimum-string-length-after-balanced-removals/

class Solution {
    fun minLengthAfterRemovals(s: String): Int {
        var a = 0
        for (c in s.toCharArray()) { if (c == 'a') a += 1 }
        var b = s.length - a
        return kotlin.math.abs(a - b)
    }
}
