// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

import java.util.HashMap

class Solution {
    fun unequalTriplets(nums: IntArray): Int {
            var cnt: MutableMap<Int, Int> = HashMap()
            for (x in nums) cnt.put(x, cnt.getOrDefault(x, 0) + 1)
            var ans: Int = 0
            var n: Int = nums.size
            var left: Int = 0
            for (c in cnt.values()) {
                var right: Int = n - left - c
                ans +=left * c * right
                left +=c
            }
            return ans
    }
}
