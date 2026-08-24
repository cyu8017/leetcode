// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

class Solution {
    fun minArrayLength(nums: IntArray, k: Int): Int {
        if (nums.size == 0) return 0
        var ans = 1
        var prod = nums[0]
        for (i in 1 until nums.size) {
            if (prod <= k && nums[i] <= k && (nums[i] == 0 || prod <= k / nums[i])) {
                prod *= nums[i]
            } else {
                ans++
                prod = nums[i]
            }
        }
        return ans
    }
}
