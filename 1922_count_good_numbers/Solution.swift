// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

class Solution {
    func countGoodNumbers(_ n: Int) -> Int {
        let MOD = 1_000_000_007
        func modPow(_ base: Int, _ exp: Int) -> Int {
            var b = base % MOD, e = exp, r = 1
            while e > 0 {
                if e & 1 == 1 { r = r * b % MOD }
                b = b * b % MOD
                e >>= 1
            }
            return r
        }
        return modPow(5, (n + 1) / 2) * modPow(4, n / 2) % MOD
    }
}
