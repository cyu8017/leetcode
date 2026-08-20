// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

class Solution {
    func minKnightMoves(_ x: Int, _ y: Int) -> Int {
        let tx = abs(x), ty = abs(y)
        var q: [(Int, Int, Int)] = [(0, 0, 0)]
        var seen = Set<Int>([0])
        let dirs = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
        var qi = 0
        while qi < q.count {
            let (r, c, d) = q[qi]; qi += 1
            if r == tx && c == ty { return d }
            for (dr, dc) in dirs {
                let nr = abs(r + dr), nc = abs(c + dc)
                if nr + nc > 300 { continue }
                let key = nr * 601 + nc
                if !seen.contains(key) {
                    seen.insert(key)
                    q.append((nr, nc, d + 1))
                }
            }
        }
        return -1
    }
}
