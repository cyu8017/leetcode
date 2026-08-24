// LeetCode 3528 - Unit Conversion I
// https://leetcode.com/problems/unit-conversion-i/

class Solution {
    func baseUnitConversions(_ conversions: [[Int]]) -> [Int] {
        let mod = 1_000_000_007
        let n = conversions.count + 1
        var g = Array(repeating: [[Int]](), count: n)
        for e in conversions { g[e[0]].append([e[1], e[2]]) }
        var ans = Array(repeating: 0, count: n)
        func dfs(_ s: Int, _ mul: Int) {
            ans[s] = mul
            for e in g[s] { dfs(e[0], (mul * e[1]) % mod) }
        }
        dfs(0, 1)
        return ans
    }
}
