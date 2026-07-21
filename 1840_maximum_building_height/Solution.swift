// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

class Solution {
    func maxBuilding(_ n: Int, _ restrictions: [[Int]]) -> Int {
        var points = [[1, 0]] + restrictions.sorted { $0[0] < $1[0] }
        if points.last![0] != n {
            points.append([n, n - 1])
        }
        for i in 1..<points.count {
            let prevId = points[i - 1][0]
            let prevHeight = points[i - 1][1]
            let currId = points[i][0]
            points[i][1] = min(points[i][1], prevHeight + currId - prevId)
        }
        for i in stride(from: points.count - 2, through: 0, by: -1) {
            let nextId = points[i + 1][0]
            let nextHeight = points[i + 1][1]
            let currId = points[i][0]
            points[i][1] = min(points[i][1], nextHeight + nextId - currId)
        }
        var best = points.map { $0[1] }.max()!
        for i in 0..<(points.count - 1) {
            let id1 = points[i][0], h1 = points[i][1]
            let id2 = points[i + 1][0], h2 = points[i + 1][1]
            best = max(best, (h1 + h2 + id2 - id1) / 2)
        }
        return best
    }
}
