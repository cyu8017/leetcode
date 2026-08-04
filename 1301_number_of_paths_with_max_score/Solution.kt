// LeetCode 1301 - Number of Paths with Max Score
// https://leetcode.com/problems/number-of-paths-with-max-score/

class Solution {
    fun pathsWithMaxScore(board: List<String>): IntArray {
        val mod = 1_000_000_007
        val n = board.size
        val score = Array(n) { IntArray(n) { -1 } }
        val ways = Array(n) { IntArray(n) }
        score[n - 1][n - 1] = 0
        ways[n - 1][n - 1] = 1
        for (r in n - 1 downTo 0) {
            for (c in n - 1 downTo 0) {
                if (board[r][c] == 'X' || (r == n - 1 && c == n - 1)) continue
                var best = -1
                var count = 0
                for ((nr, nc) in arrayOf(r + 1 to c, r to c + 1, r + 1 to c + 1)) {
                    if (nr < n && nc < n && score[nr][nc] >= 0) {
                        when {
                            score[nr][nc] > best -> {
                                best = score[nr][nc]
                                count = ways[nr][nc]
                            }
                            score[nr][nc] == best -> count = (count + ways[nr][nc]) % mod
                        }
                    }
                }
                if (best >= 0) {
                    val add = if (board[r][c].isDigit()) board[r][c] - '0' else 0
                    score[r][c] = best + add
                    ways[r][c] = count
                }
            }
        }
        return intArrayOf(maxOf(score[0][0], 0), ways[0][0])
    }
}
