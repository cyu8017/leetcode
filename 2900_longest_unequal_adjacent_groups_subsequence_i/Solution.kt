// LeetCode 2900 - Longest Unequal Adjacent Groups Subsequence I
// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

class Solution {
    fun getLongestSubsequence(words: Array<String>, groups: IntArray): MutableList<String> {
        var ans = ArrayList<String>()
        ans.add(words[0])
        var last = groups[0]
        for (i in 1 until words.size) {
            if (groups[i] != last) {
                ans.add(words[i])
                last = groups[i]
            }
        }
        return ans
    }
}
