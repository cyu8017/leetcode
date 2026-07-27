// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution {
    func minMoves(_ nums: [Int], _ limit: Int) -> Int {
        let n = nums.count
        var d = Array(repeating: 0, count: 2 * limit + 2)
        for i in 0..<(n / 2) {
            let a = nums[i], b = nums[n - 1 - i]
            let lo = min(a, b) + 1
            let hi = max(a, b) + limit
            let s = a + b
            d[2] += 2
            d[lo] -= 1
            d[s] -= 1
            d[s + 1] += 1
            d[hi + 1] += 1
        }
        var ans = Int.max
        var cur = 0
        for s in 2...(2 * limit) {
            cur += d[s]
            ans = min(ans, cur)
        }
        return ans
    }
}
