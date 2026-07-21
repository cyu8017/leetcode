// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution {
    fun countGoodSubstrings(s: String): Int {
        if (s.length < 3) return 0
        var count = 0
        for (i in 0..s.length - 3) {
            val a = s[i]
            val b = s[i + 1]
            val c = s[i + 2]
            if (a != b && b != c && a != c) count++
        }
        return count
    }
}
