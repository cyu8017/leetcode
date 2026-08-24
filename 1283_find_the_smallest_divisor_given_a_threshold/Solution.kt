// LeetCode 1283 - Find the Smallest Divisor Given a Threshold
// https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution {
    fun smallestDivisor(nums: IntArray, threshold: Int): Int {
        var lo = 1
        var hi = nums.maxOrNull()!!
        while (lo < hi) {
            val mid = (lo + hi) / 2
            var sum = 0L
            for (x in nums) sum += (x + mid - 1) / mid
            if (sum <= threshold) hi = mid else lo = mid + 1
        }
        return lo
    }
}
