// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

class Solution {
    fun reduce(nums: IntArray, fn: (Int, Int) -> Int, init: Int): Int {
        var acc = init
        for (x in nums) acc = fn(acc, x)
        return acc
    }
}
