// LeetCode 3786 - Total Sum Of Interaction Cost In Tree Groups
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/

class Solution {
    func interactionCost(_ n: Int, _ edges: [[Int]], _ group: [Int]) -> Int {
        var g = [[Int]](repeating: [], count: n)
        for e in edges {
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        }
        var total = [Int](repeating: 0, count: 21)
        for x in group { total[x] += 1 }
        var parent = [Int](repeating: -2, count: n)
        parent[0] = -1
        var order = [0]
        var i = 0
        while i < order.count {
            let u = order[i]
            for v in g[u] {
                if parent[v] == -2 {
                    parent[v] = u
                    order.append(v)
                }
            }
            i += 1
        }
        var count = Array(repeating: [Int](repeating: 0, count: 21), count: n)
        var ans = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            let u = order[i]
            count[u][group[u]] += 1
            for v in g[u] {
                if parent[v] != u { continue }
                for c in 1...20 {
                    let x = count[v][c]
                    ans += x * (total[c] - x)
                    count[u][c] += x
                }
            }
        }
        return ans
    }
}
