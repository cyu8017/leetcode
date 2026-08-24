// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

class Solution {
    fun getLargestOutlier(nums: IntArray): Int {
        var sum = 0
        val freq = HashMap<Int, Int>()
        for (x in nums) {
            sum += x
            freq[x] = (freq[x] ?: 0) + 1
        }
        var ans = Int.MIN_VALUE
        for (x in nums) {
            freq[x] = freq[x]!! - 1
            val rem = sum - x
            if (rem % 2 == 0) {
                val cand = rem / 2
                if ((freq[cand] ?: 0) > 0 && x > ans) ans = x
            }
            freq[x] = freq[x]!! + 1
        }
        return ans
    }
}
