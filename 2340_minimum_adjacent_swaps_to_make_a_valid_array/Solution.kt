// LeetCode 2340 - Minimum Adjacent Swaps to Make a Valid Array
// https://leetcode.com/problems/minimum-adjacent-swaps-to-make-a-valid-array/

class Solution {
    fun minimumSwaps(nums: IntArray): Int {
        val n = nums.size
        var minI = 0
        var maxI = 0
        for (i in 1 until n) {
            if (nums[i] < nums[minI]) minI = i
            if (nums[i] >= nums[maxI]) maxI = i
        }
        var ans = minI + (n - 1 - maxI)
        if (minI > maxI) ans--
        return ans
    }
}
