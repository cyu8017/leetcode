// LeetCode 1133 - Largest Unique Number
// https://leetcode.com/problems/largest-unique-number/

class Solution {
    func largestUniqueNumber(_ nums: [Int]) -> Int {
        var count: [Int: Int] = [:]
        for x in nums { count[x, default: 0] += 1 }
        var best = -1
        for (x, c) in count where c == 1 {
            best = max(best, x)
        }
        return best
    }
}
