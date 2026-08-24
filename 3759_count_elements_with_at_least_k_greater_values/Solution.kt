// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

class Solution {
    fun countElements(nums: IntArray, k: Int): Int {
        val n = nums.size
        if (k == 0) return n
        nums.sort()
        var ans = 0
        for (i in 0 until n - k) {
            if (nums[n - k] > nums[i]) ans++
        }
        return ans
    }
}
