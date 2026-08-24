// LeetCode 2948 - Make Lexicographically Smallest Array by Swapping Elements
// https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

class Solution {
    fun lexicographicallySmallestArray(nums: IntArray, limit: Int): IntArray {
        val n = nums.size
        val idx = Array(n) { it }
        idx.sortBy { nums[it] }
        val ans = IntArray(n)
        var i = 0
        while (i < n) {
            var j = i + 1
            while (j < n && nums[idx[j]] - nums[idx[j - 1]] <= limit) j++
            val groupIdx = IntArray(j - i) { idx[i + it] }
            groupIdx.sort()
            for (t in 0 until j - i) ans[groupIdx[t]] = nums[idx[i + t]]
            i = j
        }
        return ans
    }
}
