// LeetCode 2935 - Maximum Strong Pair XOR II
// https://leetcode.com/problems/maximum-strong-pair-xor-ii/

class Solution {
    fun maximumStrongPairXor(nums: IntArray): Int {
        nums.sort()
        var ans = 0
        for (i in nums.indices) {
            val x = nums[i]
            var j = i
            while (j < nums.size && nums[j] <= 2 * x) {
                val xorr = x xor nums[j]
                if (xorr > ans) ans = xorr
                j++
            }
        }
        return ans
    }
}
