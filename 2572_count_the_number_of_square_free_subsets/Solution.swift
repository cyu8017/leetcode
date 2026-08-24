// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

class Solution {
    func squareFreeSubsets(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        func maskOf(_ x: Int) -> Int {
            var x = x, mask = 0
            for i in 0..<primes.count {
                let p = primes[i]
                var cnt = 0
                while x % p == 0 {
                    x /= p
                    cnt += 1
                    if cnt > 1 { return -1 }
                }
                if cnt == 1 { mask |= 1 << i }
            }
            return mask
        }
        var freq = [Int: Int]()
        for x in nums { freq[x, default: 0] += 1 }
        var dp = [Int](repeating: 0, count: 1 << 10)
        dp[0] = 1
        for (x, c) in freq {
            if x == 1 { continue }
            let m = maskOf(x)
            if m < 0 { continue }
            for state in stride(from: (1 << 10) - 1, through: 0, by: -1) {
                if state & m == 0 {
                    dp[state | m] = (dp[state | m] + dp[state] * c) % MOD
                }
            }
        }
        var ans = dp.reduce(0) { ($0 + $1) % MOD }
        let ones = freq[1, default: 0]
        var mul = 1
        for _ in 0..<ones { mul = mul * 2 % MOD }
        ans = ans * mul % MOD
        return (ans - 1 + MOD) % MOD
    }
}
