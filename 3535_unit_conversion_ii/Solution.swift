// LeetCode 3535 - Unit Conversion II
// https://leetcode.com/problems/unit-conversion-ii/

class Solution {
    let MOD = 1_000_000_007

    func qpow(_ x0: Int, _ n0: Int) -> Int {
        var x = x0, n = n0, res = 1
        while n > 0 {
            if (n & 1) != 0 { res = res * x % MOD }
            x = x * x % MOD
            n >>= 1
        }
        return res
    }

    func queryConversions(_ conversions: [[Int]], _ queries: [[Int]]) -> [Int] {
        let n = conversions.count + 1
        var g = Array(repeating: [[Int]](), count: n)
        for e in conversions { g[e[0]].append([e[1], e[2]]) }
        var res = Array(repeating: 0, count: n)
        func dfs(_ s: Int, _ mul: Int) {
            res[s] = mul
            for e in g[s] { dfs(e[0], mul * e[1] % MOD) }
        }
        dfs(0, 1)
        return queries.map { res[$0[1]] * qpow(res[$0[0]], MOD - 2) % MOD }
    }
}
