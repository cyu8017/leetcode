// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

class Solution {
    func snakesAndLadders(_ board: [[Int]]) -> Int {
        let n = board.count
        let target = n * n
        func pos(_ square: Int) -> (Int, Int) {
            let s = square - 1
            let row = s / n
            let rem = s % n
            let r = n - 1 - row
            let c = row % 2 == 0 ? rem : n - 1 - rem
            return (r, c)
        }
        var q = [1]
        var seen = Array(repeating: false, count: target + 1)
        seen[1] = true
        var moves = 0
        var qi = 0
        while qi < q.count {
            let sz = q.count - qi
            for _ in 0..<sz {
                let cur = q[qi]
                qi += 1
                if cur == target { return moves }
                let lim = min(cur + 6, target)
                if cur + 1 <= lim {
                    for nxt in (cur + 1)...lim {
                        let rc = pos(nxt)
                        let dest = board[rc.0][rc.1] != -1 ? board[rc.0][rc.1] : nxt
                        if !seen[dest] {
                            seen[dest] = true
                            q.append(dest)
                        }
                    }
                }
            }
            moves += 1
        }
        return -1
    }
}
