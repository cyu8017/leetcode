// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

class Solution {
    func minCost(_ nums: [Int], _ x: Int) -> Int {
        let n = nums.count
        var best = nums
        var ans = nums.reduce(0, +)
        for rot in 1..<n {
            var cur = rot * x
            for i in 0..<n {
                best[i] = min(best[i], nums[(i + rot) % n])
                cur += best[i]
            }
            ans = min(ans, cur)
        }
        return ans
    }
}
