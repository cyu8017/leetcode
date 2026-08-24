// LeetCode 0847 - Shortest Path Visiting All Nodes
// https://leetcode.com/problems/shortest-path-visiting-all-nodes/

class Solution {
    func shortestPathLength(_ graph: [[Int]]) -> Int {
        let n = graph.count
        let target = (1 << n) - 1
        var queue = [(Int, Int, Int)]()
        var seen = Set<Int>()
        for i in 0..<n {
            queue.append((i, 1 << i, 0))
            seen.insert((i << 20) | (1 << i))
        }
        var qi = 0
        while qi < queue.count {
            let (node, mask, dist) = queue[qi]
            qi += 1
            if mask == target { return dist }
            for nxt in graph[node] {
                let nmask = mask | (1 << nxt)
                let state = (nxt << 20) | nmask
                if seen.insert(state).inserted {
                    queue.append((nxt, nmask, dist + 1))
                }
            }
        }
        return -1
    }
}
