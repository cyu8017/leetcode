// LeetCode 3405 - Count the Number of Arrays with K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

class Solution {
    func countGoodArrays(_ n: Int, _ m: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        return comb(n - 1, k, mod) * m % mod * modPow(m - 1, n - 1 - k, mod) % mod
    }

    private func modPow(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var r = 1, a = ((a % mod) + mod) % mod, e = e
        if a < 0 { a = 0 }
        while e > 0 {
            if e & 1 != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }

    private func comb(_ n: Int, _ k: Int, _ mod: Int) -> Int {
        if k < 0 || k > n { return 0 }
        var num = 1, den = 1
        if k > 0 {
            for i in 0..<k {
                num = num * (n - i) % mod
                den = den * (i + 1) % mod
            }
        }
        return num * modPow(den, mod - 2, mod) % mod
    }
}
