// LeetCode 3801 - Minimum Cost To Merge Sorted Lists
// https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/

class Solution {
    func minMergeCost(_ lists: [[Int]]) -> Int {
        let m = lists.count
        let totalMasks = 1 << m
        var merged = [[Int]](repeating: [], count: totalMasks)
        var length = [Int](repeating: 0, count: totalMasks)
        var median = [Int](repeating: 0, count: totalMasks)
        if totalMasks > 1 {
            for mask in 1..<totalMasks {
                let bit = mask & -mask
                let index = trailingZeros(bit)
                let previous = merged[mask ^ bit]
                let current = lists[index]
                var out = [Int]()
                var i = 0, j = 0
                while i < previous.count || j < current.count {
                    if j == current.count || (i < previous.count && previous[i] <= current[j]) {
                        out.append(previous[i])
                        i += 1
                    } else {
                        out.append(current[j])
                        j += 1
                    }
                }
                merged[mask] = out
                length[mask] = out.count
                median[mask] = out[(out.count - 1) / 2]
            }
        }
        let INF = 1 << 62
        var dp = [Int](repeating: 0, count: totalMasks)
        if totalMasks > 1 {
            for mask in 1..<totalMasks {
                if (mask & (mask - 1)) == 0 { continue }
                dp[mask] = INF
                let firstBit = mask & -mask
                var left = (mask - 1) & mask
                while left > 0 {
                    if (left & firstBit) != 0 {
                        let right = mask ^ left
                        if right != 0 {
                            var diff = median[left] - median[right]
                            if diff < 0 { diff = -diff }
                            let candidate = dp[left] + dp[right] + length[mask] + diff
                            if candidate < dp[mask] { dp[mask] = candidate }
                        }
                    }
                    left = (left - 1) & mask
                }
            }
        }
        return dp[totalMasks - 1]
    }

    private func trailingZeros(_ x: Int) -> Int {
        var x = x, n = 0
        while x > 0 && (x & 1) == 0 { x >>= 1; n += 1 }
        return n
    }
}
