// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

class Solution {
    func countCombinations(_ pieces: [String], _ positions: [[Int]]) -> Int {
        let dirs: [String: [(Int, Int)]] = [
            "rook": [(1, 0), (-1, 0), (0, 1), (0, -1)],
            "bishop": [(1, 1), (1, -1), (-1, 1), (-1, -1)],
            "queen": [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        ]
        let n = pieces.count
        var allMoves = [[(Int, Int, Int)]](repeating: [], count: n)
        for i in 0..<n {
            var ms = [(0, 0, 0)]
            let r = positions[i][0], c = positions[i][1]
            for (dr, dc) in dirs[pieces[i]]! {
                var nr = r + dr, nc = c + dc, step = 1
                while nr >= 1 && nr <= 8 && nc >= 1 && nc <= 8 {
                    ms.append((dr, dc, step))
                    nr += dr; nc += dc; step += 1
                }
            }
            allMoves[i] = ms
        }
        var chosen = [(Int, Int, Int)](repeating: (0, 0, 0), count: n)
        var ans = 0
        func okCombo(_ end: Int) -> Bool {
            var maxT = 0
            for i in 0...end { maxT = max(maxT, chosen[i].2) }
            if maxT == 0 { return true }
            for t in 1...maxT {
                var seen = Set<Int>()
                for i in 0...end {
                    let m = chosen[i]
                    let pr: Int, pc: Int
                    if m.2 == 0 {
                        pr = positions[i][0]; pc = positions[i][1]
                    } else {
                        let use = min(t, m.2)
                        pr = positions[i][0] + m.0 * use
                        pc = positions[i][1] + m.1 * use
                    }
                    let key = pr * 16 + pc
                    if seen.contains(key) { return false }
                    seen.insert(key)
                }
            }
            return true
        }
        func dfs(_ i: Int) {
            if i == n { ans += 1; return }
            for m in allMoves[i] {
                chosen[i] = m
                if okCombo(i) { dfs(i + 1) }
            }
        }
        dfs(0)
        return ans
    }
}
