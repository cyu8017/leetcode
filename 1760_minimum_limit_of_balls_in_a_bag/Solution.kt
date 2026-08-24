// LeetCode 1760 - Minimum Limit of Balls in a Bag
// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

class Solution {
    fun minimumSize(nums: IntArray, maxOperations: Int): Int {
        var lo = 1
        var hi = nums.max()
        while (lo < hi) {
            val mid = (lo + hi) / 2
            var ops = 0L
            for (x in nums) {
                ops += (x - 1) / mid
            }
            if (ops <= maxOperations) {
                hi = mid
            } else {
                lo = mid + 1
            }
        }
        return lo
    }
}
