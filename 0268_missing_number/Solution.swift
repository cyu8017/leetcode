// LeetCode 0268 - Missing Number
// https://leetcode.com/problems/missing-number/

class Solution {
    func missingNumber(_ nums: [Int]) -> Int {
        let length = nums.count
        let expected = length * (length + 1) / 2
        return expected - nums.reduce(0, +)
    }
}
