// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

class Solution {
    func countPartitions(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let sum = nums.reduce(0, +)
        if sum < 2 * k { return 0 }
        var dp = [Int](repeating: 0, count: k)
        dp[0] = 1
        for x in nums {
            if x < k {
                for s in stride(from: k - 1, through: x, by: -1) {
                    dp[s] = (dp[s] + dp[s - x]) % MOD
                }
            }
        }
        let bad = dp.reduce(0) { ($0 + $1) % MOD }
        var total = 1
        for _ in nums { total = total * 2 % MOD }
        return (total - 2 * bad % MOD + MOD) % MOD
    }
}
