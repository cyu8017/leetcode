// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        let n = nums.count
        var memo = [Int](repeating: -1, count: 1 << n)

        func gcd(_ a: Int, _ b: Int) -> Int {
            var (x, y) = (a, b)
            while y != 0 {
                (x, y) = (y, x % y)
            }
            return x
        }

        func dp(_ mask: Int) -> Int {
            if mask == (1 << n) - 1 { return 0 }
            if memo[mask] != -1 { return memo[mask] }
            let step = mask.nonzeroBitCount / 2 + 1
            var best = 0
            for i in 0..<n where mask >> i & 1 == 0 {
                for j in (i + 1)..<n where mask >> j & 1 == 0 {
                    let score = step * gcd(nums[i], nums[j]) + dp(mask | 1 << i | 1 << j)
                    best = max(best, score)
                }
            }
            memo[mask] = best
            return best
        }

        return dp(0)
    }
}
