// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution {
    func findNumberOfLIS(_ nums: [Int]) -> Int {
        let n = nums.count
        var lengths = Array(repeating: 1, count: n)
        var counts = Array(repeating: 1, count: n)
        for i in 0..<n {
            for j in 0..<i where nums[j] < nums[i] {
                if lengths[j] + 1 > lengths[i] {
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                } else if lengths[j] + 1 == lengths[i] {
                    counts[i] += counts[j]
                }
            }
        }
        let longest = lengths.max() ?? 0
        var answer = 0
        for i in 0..<n where lengths[i] == longest { answer += counts[i] }
        return answer
    }
}
