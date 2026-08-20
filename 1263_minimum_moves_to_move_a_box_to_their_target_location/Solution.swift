// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

class Solution {
    func minPushBox(_ grid: [[Character]]) -> Int {
        let m = grid.count, n = grid[0].count
        var box = (0, 0), person = (0, 0), target = (0, 0)
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == "B" { box = (i, j) }
                if grid[i][j] == "S" { person = (i, j) }
                if grid[i][j] == "T" { target = (i, j) }
            }
        }
        func passable(_ r: Int, _ c: Int) -> Bool {
            r >= 0 && r < m && c >= 0 && c < n && grid[r][c] != "#"
        }
        func canReach(_ start: (Int, Int), _ goal: (Int, Int), _ boxPos: (Int, Int)) -> Bool {
            var seen = Set<Int>()
            var q = [start]
            var qi = 0
            seen.insert(start.0 * n + start.1)
            let dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            while qi < q.count {
                let cur = q[qi]; qi += 1
                if cur == goal { return true }
                for (dr, dc) in dirs {
                    let nr = cur.0 + dr, nc = cur.1 + dc
                    let key = nr * n + nc
                    if passable(nr, nc) && (nr, nc) != boxPos && !seen.contains(key) {
                        seen.insert(key)
                        q.append((nr, nc))
                    }
                }
            }
            return false
        }
        var q: [(Int, Int, Int, Int, Int)] = [(box.0, box.1, person.0, person.1, 0)]
        var seen = Set<String>()
        seen.insert("\(box.0),\(box.1),\(person.0),\(person.1)")
        var qi = 0
        let dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while qi < q.count {
            let (br, bc, pr, pc, dist) = q[qi]; qi += 1
            if (br, bc) == target { return dist }
            for (dr, dc) in dirs {
                let nbr = br + dr, nbc = bc + dc
                let pushFrom = (br - dr, bc - dc)
                if passable(nbr, nbc) && passable(pushFrom.0, pushFrom.1)
                    && canReach((pr, pc), pushFrom, (br, bc)) {
                    let key = "\(nbr),\(nbc),\(br),\(bc)"
                    if !seen.contains(key) {
                        seen.insert(key)
                        q.append((nbr, nbc, br, bc, dist + 1))
                    }
                }
            }
        }
        return -1
    }
}
