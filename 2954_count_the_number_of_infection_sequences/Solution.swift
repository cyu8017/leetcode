// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

class Solution {
    private let mod = 1_000_000_007

    func numberOfSequence(_ n: Int, _ sick: [Int]) -> Int {
        var fact = Array(repeating: 0, count: n + 1)
        var invFact = Array(repeating: 0, count: n + 1)
        fact[0] = 1
        for i in 1...n { fact[i] = fact[i - 1] * i % mod }
        invFact[n] = modPow(fact[n], mod - 2)
        for i in stride(from: n, through: 1, by: -1) {
            invFact[i - 1] = invFact[i] * i % mod
        }
        let totalEmpty = n - sick.count
        var ans = fact[totalEmpty]
        var prev = -1
        for s in sick {
            let gap = s - prev - 1
            if prev == -1 {
                ans = ans * invFact[gap] % mod
            } else if gap > 0 {
                ans = ans * invFact[gap] % mod * modPow(2, gap - 1) % mod
            }
            prev = s
        }
        let gap2 = n - prev - 1
        ans = ans * invFact[gap2] % mod
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
