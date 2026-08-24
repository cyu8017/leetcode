// LeetCode 4002 - Count Valid Sequences
// https://leetcode.com/problems/count-valid-sequences/


class Solution {
    private static let MX = 500001
    private static let MOD = 1_000_000_007
    private static let tables: ([Int], [Int]) = {
        var f = Array(repeating: 0, count: MX)
        var g = Array(repeating: 0, count: MX)
        f[0] = 1
        g[0] = 1
        func modPow(_ a0: Int, _ b0: Int) -> Int {
            var a = a0 % MOD, b = b0, res = 1
            while b > 0 {
                if (b & 1) != 0 { res = res * a % MOD }
                a = a * a % MOD
                b >>= 1
            }
            return res
        }
        for i in 1..<MX {
            f[i] = f[i - 1] * i % MOD
            g[i] = modPow(f[i], MOD - 2)
        }
        return (f, g)
    }()

    func countValidSequences(_ n: Int, _ k: Int) -> Int {
        let MOD = Solution.MOD
        let (f, g) = Solution.tables
        func comb(_ n: Int, _ k: Int) -> Int {
            if k < 0 || k > n { return 0 }
            return f[n] * g[k] % MOD * g[n - k] % MOD
        }
        var ans = comb(n - 1, k - 1)
        if (n + k) % 2 == 0 {
            ans = (ans - comb((n + k) / 2 - 1, k - 1) + MOD) % MOD
        }
        return ans
    }
}
