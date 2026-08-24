// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution {
    func numberOfWays(_ startPos: Int, _ endPos: Int, _ k: Int) -> Int {
        let mod = 1_000_000_007
        let diff = abs(endPos - startPos)
        if diff > k || (k - diff) % 2 != 0 { return 0 }
        let r = (k + diff) / 2
        func modPow(_ a: Int, _ e: Int) -> Int {
            var res = 1, base = a % mod, e = e
            while e > 0 {
                if e & 1 != 0 { res = res * base % mod }
                base = base * base % mod
                e >>= 1
            }
            return res
        }
        if r < 0 || r > k { return 0 }
        var num = 1, den = 1
        if r > 0 {
            for i in 0..<r {
                num = num * (k - i) % mod
                den = den * (i + 1) % mod
            }
        }
        return num * modPow(den, mod - 2) % mod
    }
}
