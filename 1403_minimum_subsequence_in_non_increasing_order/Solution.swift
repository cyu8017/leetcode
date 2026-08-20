// LeetCode 1403 - Minimum Subsequence in Non-Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution {
    func minSubsequence(_ nums: [Int]) -> [Int] {
        var answer = [Int](), chosen = 0
        let total = nums.reduce(0, +)
        for value in nums.sorted(by: >) {
            answer.append(value)
            chosen += value
            if chosen > total - chosen { return answer }
        }
        return answer
    }
}
