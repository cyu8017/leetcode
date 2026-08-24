// LeetCode 3562 - Maximum Profit from Trading Stocks with Discounts
// https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/

class Solution {
    var g = [[Int]]()
    var present = [Int]()
    var future = [Int]()
    var budget = 0

    func dfs(_ u: Int) -> [[Int]] {
        var nxt = Array(repeating: [0, 0], count: budget + 1)
        for v in g[u] {
            let fv = dfs(v)
            for j in stride(from: budget, through: 0, by: -1) {
                for jv in 0...j {
                    for pre in 0..<2 {
                        nxt[j][pre] = max(nxt[j][pre], nxt[j - jv][pre] + fv[jv][pre])
                    }
                }
            }
        }
        var f = Array(repeating: [0, 0], count: budget + 1)
        let price = future[u - 1]
        for j in 0...budget {
            for pre in 0..<2 {
                let cost = present[u - 1] / (pre + 1)
                if j >= cost {
                    let buyProfit = nxt[j - cost][1] + (price - cost)
                    f[j][pre] = max(nxt[j][0], buyProfit)
                } else {
                    f[j][pre] = nxt[j][0]
                }
            }
        }
        return f
    }

    func maxProfit(_ n: Int, _ present: [Int], _ future: [Int], _ hierarchy: [[Int]], _ budget: Int) -> Int {
        self.present = present
        self.future = future
        self.budget = budget
        g = Array(repeating: [], count: n + 1)
        for e in hierarchy { g[e[0]].append(e[1]) }
        return dfs(1)[budget][0]
    }
}
