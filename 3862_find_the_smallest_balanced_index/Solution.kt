// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

class Solution {
    fun smallestBalancedIndex(nums: IntArray): Int {
        var s = 0
        var p = 1
        for (x in nums) { s += x }
        for (i in nums.size - 1 downTo 0) {
            s -= nums[i]
            if (s == p) return i
            p *= nums[i]
            if (p >= s) break
        }
        return -1
    }
}
