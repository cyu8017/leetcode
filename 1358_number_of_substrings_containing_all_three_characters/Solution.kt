// LeetCode 1358 - Number of Substrings Containing All Three Characters
// https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution {
    fun numberOfSubstrings(s: String): Int {
        val last = intArrayOf(-1, -1, -1)
        var ans = 0
        for (i in s.indices) {
            last[s[i] - 'a'] = i
            ans += last.minOrNull()!! + 1
        }
        return ans
    }
}
