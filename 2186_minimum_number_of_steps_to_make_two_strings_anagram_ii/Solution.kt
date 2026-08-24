// LeetCode 2186 - Minimum Number of Steps to Make Two Strings Anagram II
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/

class Solution {
    fun minSteps(s: String, t: String): Int {
        var freq: IntArray = IntArray(26)
        for (i in 0 until s.length) freq[s[i] - 'a']++
        for (i in 0 until t.length) freq[t[i] - 'a']--
        var ans: Int = 0
        for (v in freq) ans += kotlin.math.abs(v)
        return ans
    }
}
