// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

class Solution {
    func numberOfGoodSubsets(_ nums: [Int]) -> Int {
        let MOD = 1_000_000_007
        let primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        var masks = Array(repeating: 0, count: 31)
        for x in 2..<31 {
            var m = 0, y = x, ok = true
            for (i, p) in primes.enumerated() {
                if y % p == 0 {
                    if (y / p) % p == 0 { ok = false; break }
                    m |= 1 << i
                    y /= p
                }
            }
            masks[x] = ok ? m : -1
        }
        var cnt = Array(repeating: 0, count: 31)
        for v in nums { cnt[v] += 1 }
        var dp = Array(repeating: 0, count: 1 << primes.count)
        dp[0] = 1
        for x in 2..<31 {
            if cnt[x] == 0 || masks[x] < 0 { continue }
            let m = masks[x]
            for state in stride(from: (1 << primes.count) - 1, through: 0, by: -1) {
                if state & m != 0 { continue }
                dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % MOD
            }
        }
        var ans = dp[1...].reduce(0, +) % MOD
        func modPow(_ base: Int, _ exp: Int) -> Int {
            var b = base % MOD, e = exp, r = 1
            while e > 0 {
                if e & 1 == 1 { r = r * b % MOD }
                b = b * b % MOD
                e >>= 1
            }
            return r
        }
        ans = ans * modPow(2, cnt[1]) % MOD
        return ans
    }
}
