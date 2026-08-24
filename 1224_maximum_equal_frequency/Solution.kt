// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

class Solution {
    fun maxEqualFreq(nums: IntArray): Int {
        val count = mutableMapOf<Int, Int>()
        val freq = mutableMapOf<Int, Int>()
        var answer = 0
        for (i in nums.indices) {
            val x = nums[i]
            val old = count.getOrDefault(x, 0)
            if (old > 0) freq[old] = freq.getOrDefault(old, 0) - 1
            count[x] = old + 1
            freq[old + 1] = freq.getOrDefault(old + 1, 0) + 1
            val high = freq.keys.filter { freq[it]!! > 0 }.maxOrNull() ?: 0
            if (high == 1
                || freq.getOrDefault(high, 0) * high + 1 == i + 1
                || (freq.getOrDefault(high, 0) == 1 && (high - 1) * freq.getOrDefault(high - 1, 0) + high == i + 1)
            ) {
                answer = i + 1
            }
        }
        return answer
    }
}
