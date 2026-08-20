// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

class Solution {
    func minNonZeroProduct(_ p: Int) -> Int {
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
        let mx = (1 << p) - 1
        return mx % MOD * modPow(mx - 1, (1 << (p - 1)) - 1) % MOD
    }
}
