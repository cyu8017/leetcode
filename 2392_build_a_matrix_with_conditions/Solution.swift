// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

class Solution {
    func buildMatrix(_ k: Int, _ rowConditions: [[Int]], _ colConditions: [[Int]]) -> [[Int]] {
        func topo(_ conds: [[Int]]) -> [Int]? {
            var g = [[Int]](repeating: [], count: k + 1)
            var indeg = [Int](repeating: 0, count: k + 1)
            for c in conds {
                g[c[0]].append(c[1])
                indeg[c[1]] += 1
            }
            var q: [Int] = []
            for i in 1...k where indeg[i] == 0 { q.append(i) }
            var order = [Int]()
            var i = 0
            while i < q.count {
                let u = q[i]; i += 1
                order.append(u)
                for v in g[u] {
                    indeg[v] -= 1
                    if indeg[v] == 0 { q.append(v) }
                }
            }
            return order.count == k ? order : nil
        }
        guard let rowOrder = topo(rowConditions), let colOrder = topo(colConditions) else { return [] }
        var rowPos = [Int](repeating: 0, count: k + 1)
        var colPos = [Int](repeating: 0, count: k + 1)
        for i in 0..<k {
            rowPos[rowOrder[i]] = i
            colPos[colOrder[i]] = i
        }
        var ans = [[Int]](repeating: [Int](repeating: 0, count: k), count: k)
        for v in 1...k { ans[rowPos[v]][colPos[v]] = v }
        return ans
    }
}
