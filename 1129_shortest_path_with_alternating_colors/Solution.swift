// LeetCode 1129 - Shortest Path with Alternating Colors
// https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution {
    func shortestAlternatingPaths(_ n: Int, _ redEdges: [[Int]], _ blueEdges: [[Int]]) -> [Int] {
        var red = [[Int]](repeating: [], count: n)
        var blue = [[Int]](repeating: [], count: n)
        for e in redEdges { red[e[0]].append(e[1]) }
        for e in blueEdges { blue[e[0]].append(e[1]) }
        var ans = [Int](repeating: -1, count: n)
        var seen = [[Bool]](repeating: [false, false], count: n)
        var queue: [(Int, Int, Int)] = [(0, 0, 0), (0, 1, 0)]
        seen[0][0] = true
        seen[0][1] = true
        var qi = 0
        while qi < queue.count {
            let (node, color, dist) = queue[qi]; qi += 1
            if ans[node] == -1 { ans[node] = dist }
            let nxts = color == 0 ? red[node] : blue[node]
            let ncolor = 1 - color
            for nxt in nxts where !seen[nxt][ncolor] {
                seen[nxt][ncolor] = true
                queue.append((nxt, ncolor, dist + 1))
            }
        }
        return ans
    }
}
