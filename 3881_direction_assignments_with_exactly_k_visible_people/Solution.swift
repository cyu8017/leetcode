// LeetCode 3881 - Direction Assignments With Exactly K Visible People
// https://leetcode.com/problems/direction-assignments-with-exactly-k-visible-people/

class Solution {
    private static let N = 100001
    private static let MOD = 1_000_000_007
    private static let fact: [Int] = {
        var f = [Int](repeating: 1, count: N)
        for i in 1..<N { f[i] = f[i - 1] * i % MOD }
        return f
    }()
    private static let invFact: [Int] = {
        var inv = [Int](repeating: 1, count: N)
        inv[N - 1] = qmi(fact[N - 1], MOD - 2, MOD)
        for i in stride(from: N - 2, through: 1, by: -1) {
            inv[i] = inv[i + 1] * (i + 1) % MOD
        }
        return inv
    }()

    private static func qmi(_ a: Int, _ k: Int, _ p: Int) -> Int {
        var a = a, k = k, res = 1
        while k != 0 {
            if (k & 1) != 0 { res = res * a % p }
            k >>= 1
            a = a * a % p
        }
        return res
    }

    private func comb(_ n: Int, _ k: Int) -> Int {
        return Solution.fact[n] * Solution.invFact[k] % Solution.MOD * Solution.invFact[n - k] % Solution.MOD
    }

    func countVisiblePeople(_ n: Int, _ pos: Int, _ k: Int) -> Int {
        let l = pos, r = n - pos - 1
        var ans = 0
        let lim = min(k, l)
        if lim >= 0 {
            for a in 0...lim {
                let b = k - a
                if b <= r {
                    ans = (ans + 2 * comb(l, a) % Solution.MOD * comb(r, b) % Solution.MOD) % Solution.MOD
                }
            }
        }
        return ans
    }
}
