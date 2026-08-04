// LeetCode 1940
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

class Solution {
    fun longestCommonSubsequence(arrays: Array<IntArray>): List<Int> {
        val cnt = HashMap<Int, Int>()
        for (arr in arrays) for (x in arr) cnt[x] = cnt.getOrDefault(x, 0) + 1
        val m = arrays.size
        return arrays[0].filter { cnt[it] == m }
    }
}
