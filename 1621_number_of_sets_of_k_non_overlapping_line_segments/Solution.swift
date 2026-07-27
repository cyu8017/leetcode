// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

class Solution {
    func numberOfSets(_ n: Int, _ k: Int) -> Int {
        let MOD = 1_000_000_007
        return comb(n + k - 1, 2 * k, MOD)
    }

    private func comb(_ n: Int, _ k: Int, _ MOD: Int) -> Int {
        if k < 0 || k > n { return 0 }
        var k = min(k, n - k)
        var num = 1
        var den = 1
        if k == 0 { return 1 }
        for i in 0..<k {
            num = mulMod(num, n - i, MOD)
            den = mulMod(den, i + 1, MOD)
        }
        return mulMod(num, modInverse(den, MOD), MOD)
    }

    private func mulMod(_ a: Int, _ b: Int, _ MOD: Int) -> Int {
        Int((Int64(a) * Int64(b)) % Int64(MOD))
    }

    private func modInverse(_ a: Int, _ MOD: Int) -> Int {
        modPow(a, MOD - 2, MOD)
    }

    private func modPow(_ base: Int, _ exp: Int, _ MOD: Int) -> Int {
        var base = base % MOD, exp = exp, result = 1
        while exp > 0 {
            if exp & 1 == 1 { result = mulMod(result, base, MOD) }
            base = mulMod(base, base, MOD)
            exp >>= 1
        }
        return result
    }
}
