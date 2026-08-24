// LeetCode 2593 - Find Score of an Array After Marking All Elements
// https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

class Solution {
    fun findScore(nums: IntArray): Long {
        val n = nums.size
        val idx = Array(n) { it }
        idx.sortWith(compareBy({ nums[it] }, { it }))
        val marked = BooleanArray(n)
        var ans = 0L
        for (i in idx) {
            if (marked[i]) continue
            ans += nums[i]
            marked[i] = true
            if (i - 1 >= 0) marked[i - 1] = true
            if (i + 1 < n) marked[i + 1] = true
        }
        return ans
    }
}
