// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

class Solution {
    func leastBricks(_ wall: [[Int]]) -> Int {
        var edges = [Int: Int]()
        var best = 0
        for row in wall {
            var width = 0
            for i in 0..<(row.count - 1) {
                width += row[i]
                let count = (edges[width] ?? 0) + 1
                edges[width] = count
                best = max(best, count)
            }
        }
        return wall.count - best
    }
}
