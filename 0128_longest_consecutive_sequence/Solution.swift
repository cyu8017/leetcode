// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

class Solution {
    func longestConsecutive(_ nums: [Int]) -> Int {
        let values = Set(nums)
        var best = 0
        for number in values where !values.contains(number - 1) {
            var length = 1
            while values.contains(number + length) {
                length += 1
            }
            best = max(best, length)
        }
        return best
    }
}