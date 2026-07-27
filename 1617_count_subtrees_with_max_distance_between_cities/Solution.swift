// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

class Solution {
    func countSubgraphsForEachDiameter(_ n: Int, _ edges: [[Int]]) -> [Int] {
        var adj = [[Int]](repeating: [], count: n)
        for e in edges {
            let a = e[0] - 1, b = e[1] - 1
            adj[a].append(b)
            adj[b].append(a)
        }
        var ans = [Int](repeating: 0, count: n - 1)
        for mask in 1..<(1 << n) {
            if mask & (mask - 1) == 0 { continue }
            let start = (mask & -mask).trailingZeroBitCount
            func bfs(_ src: Int) -> (Int, [Int: Int]) {
                var dist = [src: 0]
                var q = [src]
                var qi = 0
                while qi < q.count {
                    let u = q[qi]; qi += 1
                    for v in adj[u] where (mask >> v) & 1 == 1 && dist[v] == nil {
                        dist[v] = dist[u]! + 1
                        q.append(v)
                    }
                }
                let far = dist.max(by: { $0.value < $1.value })!.key
                return (far, dist)
            }
            let (far, seen) = bfs(start)
            if seen.count == mask.nonzeroBitCount {
                let (_, dist) = bfs(far)
                let diameter = dist.values.max()!
                ans[diameter - 1] += 1
            }
        }
        return ans
    }
}
