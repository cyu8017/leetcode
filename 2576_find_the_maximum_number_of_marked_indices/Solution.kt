// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/

class Solution {
    fun maxNumOfMarkedIndices(nums: IntArray): Int {
        nums.sort()
        var n = nums.size
        var i = 0
        var ans = 0
        for (j in (n + 1) / 2 until n) {
            if (2 * nums[i] <= nums[j]) {
                ans += 2
                i = i + 1
            }
        }
        return ans
    }
}
