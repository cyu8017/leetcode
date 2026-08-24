// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

class Solution {
    fun advantageCount(nums1: IntArray, nums2: IntArray): IntArray {
        val sorted1 = nums1.sorted()
        val dq = ArrayDeque(sorted1)
        val ans = IntArray(nums1.size)
        val indexed = Array(nums2.size) { intArrayOf(nums2[it], it) }
        indexed.sortByDescending { it[0] }
        for (pair in indexed) {
            val `val` = pair[0]
            val i = pair[1]
            if (dq.last() > `val`) ans[i] = dq.removeLast()
            else ans[i] = dq.removeFirst()
        }
        return ans
    }
}
