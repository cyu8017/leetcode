// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

class Solution {
    func countBalancedPermutations(_ num: String) -> Int {
        let mod = 1_000_000_007
        var cnt = Array(repeating: 0, count: 10)
        var sum = 0
        for c in num {
            let d = Int(c.asciiValue! - 48)
            cnt[d] += 1
            sum += d
        }
        if sum % 2 == 1 { return 0 }
        let n = num.count
        let halfN = n / 2, halfS = sum / 2
        var fact = Array(repeating: 1, count: n + 1)
        var invF = Array(repeating: 1, count: n + 1)
        if n >= 1 {
            for i in 1...n { fact[i] = fact[i - 1] * i % mod }
        }
        invF[n] = modPow(fact[n], mod - 2, mod)
        if n >= 1 {
            for i in stride(from: n, through: 1, by: -1) { invF[i - 1] = invF[i] * i % mod }
        }
        var dp = [Int: Int]()
        dp[0] = 1
        for d in 0...9 {
            var ndp = [Int: Int]()
            for (st, ways) in dp {
                let used = st >> 32
                let s = st & ((1 << 32) - 1)
                for take in 0...cnt[d] {
                    let nu = used + take, ns = s + take * d
                    if nu > halfN || ns > halfS { continue }
                    let w = ways * invF[take] % mod * invF[cnt[d] - take] % mod
                    let nk = (nu << 32) | ns
                    ndp[nk, default: 0] = (ndp[nk, default: 0] + w) % mod
                }
            }
            dp = ndp
        }
        var ans = dp[(halfN << 32) | halfS, default: 0]
        ans = ans * fact[halfN] % mod * fact[n - halfN] % mod
        for d in 0...9 { ans = ans * fact[cnt[d]] % mod }
        return ans
    }

    private func modPow(_ a: Int, _ e: Int, _ mod: Int) -> Int {
        var r = 1, a = a % mod, e = e
        while e > 0 {
            if e & 1 != 0 { r = r * a % mod }
            a = a * a % mod
            e >>= 1
        }
        return r
    }
}
