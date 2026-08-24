// LeetCode 2113 - Elements in Array After Removing and Replacing Elements
// https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/

class Solution {
    fun elementInNums(nums: IntArray, queries: Array<IntArray>): IntArray {
        val n = nums.size
        val ans = IntArray(queries.size)
        for (i in queries.indices) {
            val t = queries[i][0]
            val idx = queries[i][1]
            val cycle = t % (2 * n)
            val size: Int
            val offset: Int
            if (cycle < n) {
                size = n - cycle
                offset = cycle
            } else {
                size = cycle - n
                offset = 0
            }
            ans[i] = if (idx >= size) -1 else nums[offset + idx]
        }
        return ans
    }
}
