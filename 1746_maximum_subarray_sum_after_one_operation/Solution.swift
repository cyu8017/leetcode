// LeetCode 1746 - Maximum Subarray Sum After One Operation
// https://leetcode.com/problems/maximum-subarray-sum-after-one-operation/

class Solution {
    func maxSumAfterOperation(_ nums: [Int]) -> Int {
        var noSquare = 0
        var oneSquare = 0
        var best = Int.min
        for value in nums {
            oneSquare = max(oneSquare + value, noSquare + value * value, value * value)
            noSquare = max(noSquare + value, value)
            best = max(best, oneSquare)
        }
        return best
    }
}
