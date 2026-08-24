// LeetCode 3550 - Smallest Index With Digit Sum Equal to Index
// https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution {
    fun smallestIndex(nums: IntArray): Int {
        for (i in 0 until nums.size) {
            var x = nums[i]
            var s = 0
            while (x > 0) {
s += x % 10
            if (s == i) return i
        }
        return -1
    }
}
x /= 10
}
