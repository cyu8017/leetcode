// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

class Solution {
    func maxValue(_ events: [[Int]], _ k: Int) -> Int {
        let sorted = events.sorted { $0.lexicographicallyPrecedes($1) }
        let n = sorted.count
        let starts = sorted.map { $0[0] }

        func upperBound(_ target: Int) -> Int {
            var lo = 0
            var hi = n
            while lo < hi {
                let mid = (lo + hi) / 2
                if starts[mid] <= target {
                    lo = mid + 1
                } else {
                    hi = mid
                }
            }
            return lo
        }

        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: k + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let j = upperBound(sorted[i][1])
            for remain in 1...k {
                dp[remain][i] = max(dp[remain][i + 1], sorted[i][2] + dp[remain - 1][j])
            }
        }
        return dp[k][0]
    }
}
