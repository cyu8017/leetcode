// LeetCode 2405 - Optimal Partition of String
// https://leetcode.com/problems/optimal-partition-of-string/

class Solution {
    fun partitionString(s: String): Int {
        var ans = 1
        var seen = 0
        for (c in s) {
            val bit = 1 shl (c - 'a')
            if ((seen and bit) != 0) {
                ans++
                seen = 0
            }
            seen = seen or bit
        }
        return ans
    }
}
