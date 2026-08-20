// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

class Solution {
    func isPrintable(_ targetGrid: [[Int]]) -> Bool {
        var colors = Set<Int>()
        for row in targetGrid { for x in row { colors.insert(x) } }
        var bounds = [Int: (Int, Int, Int, Int)]()
        for c in colors { bounds[c] = (Int.max / 4, Int.max / 4, -1, -1) }
        for (r, row) in targetGrid.enumerated() {
            for (col, c) in row.enumerated() {
                var b = bounds[c]!
                b.0 = min(b.0, r); b.1 = min(b.1, col)
                b.2 = max(b.2, r); b.3 = max(b.3, col)
                bounds[c] = b
            }
        }
        var graph = [Int: Set<Int>]()
        var indegree = [Int: Int]()
        for c in colors { indegree[c] = 0; graph[c] = [] }
        for (c, b) in bounds {
            for r in b.0...b.2 {
                for col in b.1...b.3 {
                    let other = targetGrid[r][col]
                    if other != c && !(graph[c]?.contains(other) ?? false) {
                        graph[c, default: []].insert(other)
                        indegree[other, default: 0] += 1
                    }
                }
            }
        }
        var queue = colors.filter { indegree[$0] == 0 }
        var seen = 0
        while !queue.isEmpty {
            let c = queue.removeFirst()
            seen += 1
            for nxt in graph[c] ?? [] {
                indegree[nxt]! -= 1
                if indegree[nxt] == 0 { queue.append(nxt) }
            }
        }
        return seen == colors.count
    }
}
