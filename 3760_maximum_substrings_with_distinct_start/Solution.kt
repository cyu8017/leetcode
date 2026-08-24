// LeetCode 3760 - Maximum Substrings With Distinct Start
// https://leetcode.com/problems/maximum-substrings-with-distinct-start/

class Solution {
    fun maxDistinct(s: String): Int {
        val cnt = IntArray(26)
        var ans = 0
        for (c in s) {
            cnt[c - 'a']++
            if (cnt[c - 'a'] == 1) ans++
        }
        return ans
    }
}
