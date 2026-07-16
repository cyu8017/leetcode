// LeetCode 0334 - Increasing Triplet Subsequence
// https://leetcode.com/problems/increasing-triplet-subsequence/

class Solution {
    func increasingTriplet(_ nums: [Int]) -> Bool {
        var first = Int.max
        var second = Int.max
        for num in nums {
            if num <= first {
                first = num
            } else if num <= second {
                second = num
            } else {
                return true
            }
        }
        return false
    }
}
