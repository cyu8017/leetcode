// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution {
    func getAncestors(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        var g = [[Int]](repeating: [], count: n)
        var indeg = [Int](repeating: 0, count: n)
        for e in edges {
            g[e[0]].append(e[1])
            indeg[e[1]] += 1
        }
        var anc = [Set<Int>](repeating: [], count: n)
        var q = (0..<n).filter { indeg[$0] == 0 }
        var head = 0
        while head < q.count {
            let u = q[head]; head += 1
            for v in g[u] {
                anc[v].insert(u)
                anc[v].formUnion(anc[u])
                indeg[v] -= 1
                if indeg[v] == 0 { q.append(v) }
            }
        }
        return anc.map { $0.sorted() }
    }
}
