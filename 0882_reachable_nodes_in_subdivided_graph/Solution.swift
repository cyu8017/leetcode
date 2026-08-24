// LeetCode 0882 - Reachable Nodes In Subdivided Graph
// https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

class Solution {
    func reachableNodes(_ edges: [[Int]], _ maxMoves: Int, _ n: Int) -> Int {
        var graph = Array(repeating: [Int: Int](), count: n)
        for e in edges {
            graph[e[0]][e[1]] = e[2]
            graph[e[1]][e[0]] = e[2]
        }
        var pq = [(maxMoves, 0)]
        var seen = [Int: Int]()
        while !pq.isEmpty {
            pq.sort { $0.0 > $1.0 }
            let cur = pq.removeFirst()
            let moves = cur.0, node = cur.1
            if seen[node] != nil { continue }
            seen[node] = moves
            for (nei, cnt) in graph[node] {
                let remain = moves - cnt - 1
                if seen[nei] == nil && remain >= 0 {
                    pq.append((remain, nei))
                }
            }
        }
        var ans = seen.count
        for e in edges {
            let left = seen[e[0]] ?? 0
            let right = seen[e[1]] ?? 0
            ans += min(e[2], left + right)
        }
        return ans
    }
}
