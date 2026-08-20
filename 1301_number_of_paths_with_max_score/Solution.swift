// LeetCode 1301 - Number of Paths with Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

class Solution {
    func pathsWithMaxScore(_ board: [String]) -> [Int] {
        let mod = 1_000_000_007
        let n = board.count
        var score = Array(repeating: Array(repeating: -1, count: n), count: n)
        var ways = Array(repeating: Array(repeating: 0, count: n), count: n)
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1
        let chars = board.map { Array($0) }
        for r in stride(from: n - 1, through: 0, by: -1) {
            for c in stride(from: n - 1, through: 0, by: -1) {
                if chars[r][c] == "X" || (r == n - 1 && c == n - 1) { continue }
                var best = -1, count = 0
                for (nr, nc) in [(r + 1, c), (r, c + 1), (r + 1, c + 1)] {
                    if nr < n && nc < n && score[nr][nc] >= 0 {
                        if score[nr][nc] > best {
                            best = score[nr][nc]; count = ways[nr][nc]
                        } else if score[nr][nc] == best {
                            count = (count + ways[nr][nc]) % mod
                        }
                    }
                }
                if best >= 0 {
                    let add = chars[r][c].isNumber ? Int(String(chars[r][c]))! : 0
                    score[r][c] = best + add
                    ways[r][c] = count
                }
            }
        }
        return [max(score[0][0], 0), ways[0][0]]
    }
}
