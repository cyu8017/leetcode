// LeetCode 2626 - Array Reduce Transformation
// https://leetcode.com/problems/array-reduce-transformation/

class Solution {
    func reduce(_ nums: [Int], _ fn: (Int, Int) -> Int, _ initVal: Int) -> Int {
        var acc = initVal
        for x in nums { acc = fn(acc, x) }
        return acc
    }
}
