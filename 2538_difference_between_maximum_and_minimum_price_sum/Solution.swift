// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

class Solution {
    func maxOutput(_ n: Int, _ edges: [[Int]], _ price: [Int]) -> Int {
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var down = [Int](repeating: 0, count: n)
        func dfs1(_ u: Int, _ p: Int) {
            down[u] = price[u]
            for v in g[u] where v != p {
                dfs1(v, u)
                down[u] = max(down[u], down[v] + price[u])
            }
        }
        dfs1(0, -1)
        var ans = 0
        func dfs2(_ u: Int, _ p: Int, _ up: Int) {
            ans = max(ans, down[u] - price[u], up - price[u])
            var cands = [up]
            for v in g[u] where v != p {
                cands.append(down[v] + price[u])
            }
            cands.sort(by: >)
            for v in g[u] where v != p {
                var best = cands[0]
                if best == down[v] + price[u] && cands.count > 1 {
                    best = cands[1]
                }
                dfs2(v, u, price[v] + best)
            }
        }
        dfs2(0, -1, price[0])
        return ans
    }
}
