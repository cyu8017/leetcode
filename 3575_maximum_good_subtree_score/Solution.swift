// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

class Solution {
    let MOD = 1_000_000_007
    var g = [[Int]]()
    var vals = [Int]()
    var ans = 0

    func digitMask(_ x0: Int) -> [Int] {
        var x = x0
        let v = x
        var mask = 0
        if x == 0 { return [1, 1, 0] }
        while x > 0 {
            let d = x % 10
            if (mask & (1 << d)) != 0 { return [0, 0, 0] }
            mask |= 1 << d
            x /= 10
        }
        return [mask, 1, v]
    }

    func dfs(_ u: Int) -> [Int: Int] {
        var dp = [0: 0]
        let dm = digitMask(vals[u])
        if dm[1] == 1 { dp[dm[0]] = dm[2] }
        for c in g[u] {
            let child = dfs(c)
            var ndp = [Int: Int]()
            for (k1, v1) in dp {
                for (k2, v2) in child {
                    if (k1 & k2) == 0 {
                        let nm = k1 | k2
                        ndp[nm] = max(ndp[nm] ?? 0, v1 + v2)
                    }
                }
            }
            for (k, v) in dp { ndp[k] = max(ndp[k] ?? 0, v) }
            for (k, v) in child { ndp[k] = max(ndp[k] ?? 0, v) }
            dp = ndp
        }
        var best = 0
        for s in dp.values { best = max(best, s) }
        ans = (ans + best) % MOD
        return dp
    }

    func goodSubtreeSum(_ vals: [Int], _ par: [Int]) -> Int {
        let n = vals.count
        self.vals = vals
        g = Array(repeating: [], count: n)
        if n > 1 {
            for i in 1..<n { g[par[i]].append(i) }
        }
        ans = 0
        _ = dfs(0)
        return ans
    }
}
