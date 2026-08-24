// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

class Solution {
    private let mod = 1_000_000_007

    func stringCount(_ n: Int) -> Int {
        if n < 4 { return 0 }
        var ans = modPow(26, n)
        ans = (ans - 3 * modPow(25, n) % mod + mod) % mod
        ans = (ans + 3 * modPow(24, n) % mod) % mod
        ans = (ans - modPow(23, n) + mod) % mod
        ans = (ans + n % mod * modPow(25, n - 1) % mod) % mod
        ans = (ans - 2 * (n % mod) % mod * modPow(24, n - 1) % mod + mod) % mod
        ans = (ans + n % mod * modPow(23, n - 1) % mod) % mod
        ans = (ans - n % mod * ((n - 1 + mod) % mod) % mod * modPow(24, n - 2) % mod + mod) % mod
        ans = (ans + n % mod * ((n - 1 + mod) % mod) % mod * modPow(23, n - 2) % mod) % mod
        return ans
    }

    private func modPow(_ a0: Int, _ b0: Int) -> Int {
        var a = a0 % mod, b = b0, res = 1
        while b > 0 {
            if b & 1 != 0 { res = res * a % mod }
            a = a * a % mod
            b >>= 1
        }
        return res
    }
}
