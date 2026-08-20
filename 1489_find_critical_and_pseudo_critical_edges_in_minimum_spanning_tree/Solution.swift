// LeetCode 1489 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

class Solution {
    func findCriticalAndPseudoCriticalEdges(_ n: Int, _ edges: [[Int]]) -> [[Int]] {
        let es = edges.enumerated().map { ($0.element[2], $0.element[0], $0.element[1], $0.offset) }.sorted { $0.0 < $1.0 }
        func mst(_ skip: Int = -1, _ force: Int = -1) -> Int {
            var parent = Array(0..<n)
            func find(_ x: Int) -> Int {
                var x = x
                while x != parent[x] { parent[x] = parent[parent[x]]; x = parent[x] }
                return x
            }
            var total = 0, used = 0
            if force >= 0 {
                let (w, a, b, _) = es[force]
                parent[find(a)] = find(b); total += w; used += 1
            }
            for (j, e) in es.enumerated() {
                if j == skip || j == force { continue }
                let (w, a, b, _) = e
                let x = find(a), y = find(b)
                if x != y { parent[x] = y; total += w; used += 1 }
            }
            return used == n - 1 ? total : Int.max / 4
        }
        let base = mst()
        var critical = [Int](), pseudo = [Int]()
        for j in 0..<es.count {
            if mst(j, -1) > base { critical.append(es[j].3) }
            else if mst(-1, j) == base { pseudo.append(es[j].3) }
        }
        return [critical.sorted(), pseudo.sorted()]
    }
}
