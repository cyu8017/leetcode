// LeetCode 3428 - Maximum and Minimum Sums of at Most Size K Subsequences
// https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/

class Solution {
    func minMaxSums(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        let nums = nums.sorted()
        let n = nums.count
        var C = Array(repeating: Array(repeating: 0, count: k), count: n + 1)
        for i in 0...n {
            C[i][0] = 1
            var j = 1
            while j < k && j <= i {
                C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % mod
                j += 1
            }
        }
        var ans = 0
        for i in 0..<n {
            var waysMax = 0
            var j = 0
            while j < k && j <= i {
                waysMax = (waysMax + C[i][j]) % mod
                j += 1
            }
            var waysMin = 0
            let right = n - i - 1
            j = 0
            while j < k && j <= right {
                waysMin = (waysMin + C[right][j]) % mod
                j += 1
            }
            ans = (ans + nums[i] * waysMax % mod + nums[i] * waysMin % mod) % mod
        }
        return ans
    }
}
