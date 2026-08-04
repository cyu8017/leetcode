// LeetCode 1915 - Number Of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution {
    fun wonderfulSubstrings(word: String): Long {
        val count = LongArray(1024)
        count[0] = 1
        var mask = 0
        var ans = 0L
        for (ch in word) {
            mask = mask xor (1 shl (ch - 'a'))
            ans += count[mask]
            for (bit in 0 until 10) ans += count[mask xor (1 shl bit)]
            count[mask]++
        }
        return ans
    }
}
