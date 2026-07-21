// LeetCode 1862 - Sum of Floored Pairs
// https://leetcode.com/problems/sum-of-floored-pairs/

class Solution {
    fun sumOfFlooredPairs(nums: IntArray): Int {
        val mod = 1_000_000_007
        val maxVal = nums.maxOrNull()!!
        val count = IntArray(maxVal + 1)
        for (num in nums) count[num]++
        val prefix = IntArray(maxVal + 1)
        prefix[0] = count[0]
        for (value in 1..maxVal) {
            prefix[value] = prefix[value - 1] + count[value]
        }
        var answer = 0L
        for (divisor in 1..maxVal) {
            if (count[divisor] == 0) continue
            var quotient = 1
            while (quotient.toLong() * divisor <= maxVal) {
                val low = quotient * divisor
                val high = minOf((quotient + 1) * divisor - 1, maxVal)
                val matches = prefix[high] - if (low > 0) prefix[low - 1] else 0
                answer = (answer + count[divisor].toLong() * matches * quotient) % mod
                quotient++
            }
        }
        return answer.toInt()
    }
}
