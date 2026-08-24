// LeetCode 3539 - Find Sum of Array Product of Magical Sequences
// https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/

class Solution {
    let N = 31
    let MOD = 1_000_000_007
    var f = [Int]()
    var g = [Int]()
    var inited = false
    var dp = [[[[Int]]]]()
    var nums = [Int]()
    var n = 0

    func qpow(_ a0: Int, _ k0: Int) -> Int {
        var a = a0, k = k0, res = 1
        while k > 0 {
            if (k & 1) != 0 { res = res * a % MOD }
            a = a * a % MOD
            k >>= 1
        }
        return res
    }

    func initFact() {
        if inited { return }
        f = Array(repeating: 0, count: N)
        g = Array(repeating: 0, count: N)
        f[0] = 1; g[0] = 1
        for i in 1..<N {
            f[i] = f[i - 1] * i % MOD
            g[i] = qpow(f[i], MOD - 2)
        }
        inited = true
    }

    func comb(_ m: Int, _ nn: Int) -> Int {
        if nn < 0 || nn > m { return 0 }
        return f[m] * g[nn] % MOD * g[m - nn] % MOD
    }

    func dfs(_ i: Int, _ j: Int, _ kk: Int, _ st: Int) -> Int {
        if kk < 0 || (i == n && j > 0) { return 0 }
        if i == n {
            var st = st, kk = kk
            while st > 0 { kk -= st & 1; st >>= 1 }
            return kk == 0 ? 1 : 0
        }
        if dp[i][j][kk][st] != -1 { return dp[i][j][kk][st] }
        var res = 0
        for t in 0...j {
            let nt = t + st
            let nk = kk - (nt & 1)
            let p = qpow(nums[i], t)
            let tmp = comb(j, t) * p % MOD * dfs(i + 1, j - t, nk, nt >> 1) % MOD
            res = (res + tmp) % MOD
        }
        dp[i][j][kk][st] = res
        return res
    }

    func magicalSum(_ m: Int, _ k: Int, _ nums: [Int]) -> Int {
        initFact()
        self.nums = nums
        n = nums.count
        dp = Array(repeating: Array(repeating: Array(repeating: Array(repeating: -1, count: N), count: k + 1), count: m + 1), count: n + 1)
        return dfs(0, m, k, 0)
    }
}
