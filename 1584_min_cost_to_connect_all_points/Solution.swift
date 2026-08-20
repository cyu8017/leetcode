// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution {
    func minCostConnectPoints(_ points: [[Int]]) -> Int {
        let n = points.count
        var used = Array(repeating: false, count: n)
        var dist = Array(repeating: Int.max / 4, count: n)
        dist[0] = 0
        var answer = 0
        for _ in 0..<n {
            var u = -1
            for i in 0..<n where !used[i] {
                if u < 0 || dist[i] < dist[u] { u = i }
            }
            used[u] = true
            answer += dist[u]
            for v in 0..<n where !used[v] {
                let d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                dist[v] = min(dist[v], d)
            }
        }
        return answer
    }
}
