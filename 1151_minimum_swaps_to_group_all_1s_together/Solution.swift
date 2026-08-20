// LeetCode 1151 - Minimum Swaps to Group All 1's Together
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/

class Solution {
    func minSwaps(_ data: [Int]) -> Int {
        let ones = data.reduce(0, +)
        if ones <= 1 { return 0 }
        var cur = data.prefix(ones).reduce(0, +)
        var best = cur
        for i in ones..<data.count {
            cur += data[i] - data[i - ones]
            best = max(best, cur)
        }
        return ones - best
    }
}
