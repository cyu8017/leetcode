// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

class Solution {
    func isEscapePossible(_ blocked: [[Int]], _ source: [Int], _ target: [Int]) -> Bool {
        var blockedSet = Set<[Int]>()
        for b in blocked { blockedSet.insert(b) }
        let limit = blocked.count * max(0, blocked.count - 1) / 2
        let bound = 1_000_000

        func bfs(_ start: [Int], _ goal: [Int]) -> Bool {
            var queue = [start]
            var seen: Set<[Int]> = [start]
            var qi = 0
            while qi < queue.count {
                if seen.count > limit { return true }
                let cur = queue[qi]; qi += 1
                if cur == goal { return true }
                let r = cur[0], c = cur[1]
                for d in [[1, 0], [-1, 0], [0, 1], [0, -1]] {
                    let nr = r + d[0], nc = c + d[1]
                    let next = [nr, nc]
                    if nr >= 0 && nr < bound && nc >= 0 && nc < bound && !blockedSet.contains(next) && !seen.contains(next) {
                        seen.insert(next)
                        queue.append(next)
                    }
                }
            }
            return false
        }
        return bfs(source, target) && bfs(target, source)
    }
}
