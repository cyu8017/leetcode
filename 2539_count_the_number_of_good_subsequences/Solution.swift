// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/

class Solution {
    func countGoodSubsequences(_ s: String) -> Int {
        let MOD = 1_000_000_007
        var cnt = [Int](repeating: 0, count: 26)
        var maxf = 0
        for c in s {
            let i = Int(c.asciiValue! - Character("a").asciiValue!)
            cnt[i] += 1
            maxf = max(maxf, cnt[i])
        }
        func modPow(_ a: Int, _ e: Int) -> Int {
            var a = a % MOD, e = e, res = 1
            while e > 0 {
                if e & 1 != 0 { res = res * a % MOD }
                a = a * a % MOD
                e >>= 1
            }
            return res
        }
        var fact = [Int](repeating: 1, count: maxf + 1)
        var invFact = [Int](repeating: 1, count: maxf + 1)
        if maxf >= 1 {
            for i in 1...maxf { fact[i] = fact[i - 1] * i % MOD }
        }
        invFact[maxf] = modPow(fact[maxf], MOD - 2)
        if maxf >= 1 {
            for i in stride(from: maxf, through: 1, by: -1) {
                invFact[i - 1] = invFact[i] * i % MOD
            }
        }
        func comb(_ n: Int, _ k: Int) -> Int {
            if k < 0 || k > n { return 0 }
            return fact[n] * invFact[k] % MOD * invFact[n - k] % MOD
        }
        var ans = 0
        if maxf >= 1 {
            for k in 1...maxf {
                var ways = 1
                for i in 0..<26 {
                    if cnt[i] >= k { ways = ways * (1 + comb(cnt[i], k)) % MOD }
                }
                ans = (ans + ways - 1 + MOD) % MOD
            }
        }
        return ans
    }
}
