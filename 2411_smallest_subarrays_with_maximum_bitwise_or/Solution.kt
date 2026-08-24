// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

class Solution {
    fun smallestSubarrays(nums: IntArray): IntArray {
        val n = nums.size
        val ans = IntArray(n)
        val last = IntArray(32) { -1 }
        for (i in n - 1 downTo 0) {
            for (b in 0 until 32) {
                if (((nums[i] shr b) and 1) != 0) last[b] = i
            }
            var far = i
            for (b in 0 until 32) far = maxOf(far, last[b])
            ans[i] = far - i + 1
        }
        return ans
    }
}
