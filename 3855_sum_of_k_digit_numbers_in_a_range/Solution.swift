// LeetCode 3855 - Sum Of K Digit Numbers In A Range
// https://leetcode.com/problems/sum-of-k-digit-numbers-in-a-range/

class Solution {
    private func qpow(_ a: Int, _ n: Int, _ mod: Int) -> Int {
        var a = a % mod, n = n, ans = 1
        while n > 0 {
            if (n & 1) != 0 { ans = ans * a % mod }
            a = a * a % mod
            n >>= 1
        }
        return ans
    }

    func sumOfNumbers(_ l: Int, _ r: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        let n = r - l + 1
        let sum = (l + r) * n / 2 % MOD
        let part1 = qpow(n % MOD, k - 1, MOD)
        let part2 = (qpow(10, k, MOD) - 1 + MOD) % MOD
        let inv9 = qpow(9, MOD - 2, MOD)
        var ans = sum
        ans = ans * part1 % MOD
        ans = ans * part2 % MOD
        ans = ans * inv9 % MOD
        return ans
    }
}
