// LeetCode 3530 - Maximum Profit from Valid Topological Order in DAG
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/

class Solution {
    func pop(_ x0: Int) -> Int {
        var x = x0, c = 0
        while x != 0 { c += x & 1; x >>= 1 }
        return c
    }

    func maxProfit(_ n: Int, _ edges: [[Int]], _ score: [Int]) -> Int {
        var need = Array(repeating: 0, count: n)
        var dp = Array(repeating: -1, count: 1 << n)
        dp[0] = 0
        for e in edges { need[e[1]] |= 1 << e[0] }
        for mask in 0..<(1 << n) {
            if dp[mask] < 0 { continue }
            let pos = pop(mask) + 1
            for i in 0..<n {
                if ((mask >> i) & 1) != 0 { continue }
                if (mask & need[i]) == need[i] {
                    let nm = mask | (1 << i)
                    let v = dp[mask] + score[i] * pos
                    if v > dp[nm] { dp[nm] = v }
                }
            }
        }
        return dp[(1 << n) - 1]
    }
}
