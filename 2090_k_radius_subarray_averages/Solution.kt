// LeetCode 2090 - K Radius Subarray Averages
// https://leetcode.com/problems/k-radius-subarray-averages/

class Solution {
    fun getAverages(nums: IntArray, k: Int): IntArray {
        var n: Int = nums.size
        var ans: IntArray = IntArray(n)
        ans.fill(-1)
        if (2 * k + 1 > n) return ans
        var sum: Long = 0
        for (i in 0 until 2 * k + 1) sum += nums[i]
        ans[k] = (sum / (2 * k + 1)).toInt()
        var i = k + 1
        while (i + k < n) {
            sum += nums[i + k] - nums[i - k - 1]
            ans[i] = (sum / (2 * k + 1)).toInt()
            i++
        }
        return ans
    }
}
