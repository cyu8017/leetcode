// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

class Solution {
    func numberOfPaths(_ n: Int, _ corridors: [[Int]]) -> Int {
        var g = [Set<Int>](repeating: [], count: n + 1)
        for e in corridors {
            g[e[0]].insert(e[1])
            g[e[1]].insert(e[0])
        }
        var ans = 0
        for e in corridors {
            for c in g[e[0]] where g[e[1]].contains(c) { ans += 1 }
        }
        return ans / 3
    }
}
