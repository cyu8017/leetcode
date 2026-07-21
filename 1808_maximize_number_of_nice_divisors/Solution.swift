// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

class Solution {
    func maxNiceDivisors(_ primeFactors: Int) -> Int {
        let mod = 1_000_000_007
        if primeFactors <= 3 { return primeFactors }
        if primeFactors % 3 == 0 {
            return modPow(3, primeFactors / 3, mod)
        }
        if primeFactors % 3 == 1 {
            return Int((Int64(modPow(3, primeFactors / 3 - 1, mod)) * 4) % Int64(mod))
        }
        return Int((Int64(modPow(3, primeFactors / 3, mod)) * 2) % Int64(mod))
    }

    private func modPow(_ base: Int, _ exp: Int, _ mod: Int) -> Int {
        var b = Int64(base % mod)
        var e = exp
        var res: Int64 = 1
        let m = Int64(mod)
        while e > 0 {
            if e & 1 == 1 { res = res * b % m }
            b = b * b % m
            e >>= 1
        }
        return Int(res)
    }
}
