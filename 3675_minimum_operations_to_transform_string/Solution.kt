// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

class Solution {
    fun minOperations(s: String): Int {
        var ans = 0
        for (c in s.toCharArray()) {
            if (c != 'a') ans = maxOf(ans, 26 - (c - 'a'))
        }
        return ans
    }
}
