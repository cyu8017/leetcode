// LeetCode 3970 - Shortest Path With At Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/


class Solution {
    func shortestPath(_ n: Int, _ edges: [[Int]], _ labels: String, _ k: Int) -> Int {
        let labs = Array(labels)
        var graph = Array(repeating: [(Int, Int)](), count: n)
        for edge in edges { graph[edge[0]].append((edge[1], edge[2])) }
        let infinity = Int.max / 4
        var distances = Array(repeating: Array(repeating: infinity, count: k + 1), count: n)
        distances[0][1] = 0
        var pq = [(0, 0, 1)]
        while !pq.isEmpty {
            pq.sort { $0.0 < $1.0 }
            let cur = pq.removeFirst()
            let distance = cur.0, node = cur.1, run = cur.2
            if distance != distances[node][run] { continue }
            if node == n - 1 { return distance }
            for (to, weight) in graph[node] {
                var nextRun = 1
                if labs[node] == labs[to] { nextRun = run + 1 }
                if nextRun > k { continue }
                let nextDistance = distance + weight
                if nextDistance < distances[to][nextRun] {
                    distances[to][nextRun] = nextDistance
                    pq.append((nextDistance, to, nextRun))
                }
            }
        }
        return -1
    }
}
