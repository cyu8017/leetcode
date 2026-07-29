// LeetCode 1005 - Maximize Sum Of Array After K Negations
// https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution {
    fun largestSumAfterKNegations(nums: IntArray, k: Int): Int {
        nums.sort()
        var kk = k
        for (i in nums.indices) {
            if (kk == 0) break
            if (nums[i] < 0) {
                nums[i] = -nums[i]
                kk--
            }
        }
        if (kk % 2 == 1) {
            nums.sort()
            nums[0] = -nums[0]
        }
        return nums.sum()
    }
}
