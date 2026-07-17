// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

class Solution {
    func canMouseWin(_ grid: [String], _ catJump: Int, _ mouseJump: Int) -> Bool {
        let cellsGrid = grid.map { Array($0) }
        let rows = cellsGrid.count
        let cols = cellsGrid[0].count
        var totalOpen = 0
        var mouse = 0
        var cat = 0
        var food = 0
        for r in 0..<rows {
            for c in 0..<cols {
                let cell = cellsGrid[r][c]
                if cell != "#" { totalOpen += 1 }
                if cell == "M" { mouse = r * cols + c }
                else if cell == "C" { cat = r * cols + c }
                else if cell == "F" { food = r * cols + c }
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        func computeMoves(_ pos: Int, _ jump: Int) -> [Int] {
            let r = pos / cols
            let c = pos % cols
            var out = [pos]
            for (dr, dc) in dirs {
                for step in 1...jump {
                    let nr = r + dr * step
                    let nc = c + dc * step
                    if nr < 0 || nr >= rows || nc < 0 || nc >= cols || cellsGrid[nr][nc] == "#" { break }
                    out.append(nr * cols + nc)
                }
            }
            return out
        }
        let cellCount = rows * cols
        var mouseMoves = [[Int]](repeating: [], count: cellCount)
        var catMoves = [[Int]](repeating: [], count: cellCount)
        for r in 0..<rows {
            for c in 0..<cols {
                if cellsGrid[r][c] != "#" {
                    let pos = r * cols + c
                    mouseMoves[pos] = computeMoves(pos, mouseJump)
                    catMoves[pos] = computeMoves(pos, catJump)
                }
            }
        }
        let maxTurn = 2 * totalOpen
        var memo = [Int8](repeating: 0, count: cellCount * cellCount * maxTurn)
        func win(_ m: Int, _ c: Int, _ turn: Int) -> Bool {
            if turn >= maxTurn { return false }
            if m == food { return true }
            if c == food || c == m { return false }
            let key = (m * cellCount + c) * maxTurn + turn
            if memo[key] != 0 { return memo[key] == 1 }
            var result: Bool
            if turn % 2 == 0 {
                result = false
                for nm in mouseMoves[m] where win(nm, c, turn + 1) {
                    result = true
                    break
                }
            } else {
                result = true
                for nc in catMoves[c] where !win(m, nc, turn + 1) {
                    result = false
                    break
                }
            }
            memo[key] = result ? 1 : 2
            return result
        }
        return win(mouse, cat, 0)
    }
}
