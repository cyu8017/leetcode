// LeetCode 3277 - Maximum XOR Score Subarray Queries
// https://leetcode.com/problems/maximum-xor-score-subarray-queries/

class Solution {
    func maximumSubarrayXor(_ nums: [Int], _ queries: [[Int]]) -> [Int] {
        let n = nums.count
        var f = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n { f[i][i] = nums[i] }
        if n >= 2 {
            for length in 2...n {
                for i in 0...(n - length) {
                    let j = i + length - 1
                    f[i][j] = f[i][j - 1] ^ f[i + 1][j]
                }
            }
        }
        var best = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n { best[i][i] = f[i][i] }
        if n >= 2 {
            for length in 2...n {
                for i in 0...(n - length) {
                    let j = i + length - 1
                    best[i][j] = max(f[i][j], max(best[i][j - 1], best[i + 1][j]))
                }
            }
        }
        return queries.map { best[$0[0]][$0[1]] }
    }
}
