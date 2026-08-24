// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

class Solution {
    func findLHS(_ nums: [Int]) -> Int {
        var counts = [Int: Int]()
        for num in nums { counts[num, default: 0] += 1 }
        var best = 0
        for (key, value) in counts {
            if let next = counts[key + 1] {
                best = max(best, value + next)
            }
        }
        return best
    }
}
