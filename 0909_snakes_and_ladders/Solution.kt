// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

class Solution {
    fun snakesAndLadders(board: Array<IntArray>): Int {
        var n = board.size
        var target = n * n
        var q = ArrayDeque()
        var seen = BooleanArray(target + 1)
        q.add(1)
        seen[1] = true
        var moves = 0
        while (!q.isEmpty()) {
            var sz = q.size
            for (s in 0 until sz) {
                var cur = q.removeFirst()
                if (cur == target) return moves
                var lim = minOf(cur + 6, target)
                for (nxt in cur + 1 until = lim) {
                    var rc = pos(nxt, n)
                    var dest = if (board[rc[0]][rc[1]] != -1) board[rc[0]][rc[1]] else nxt
                    if (!seen[dest]) {
                        seen[dest] = true
                        q.add(dest)
                    }
                }
            }
            moves++
        }
        return -1
    }

    private fun pos(square: Int, n: Int): IntArray {
        square--
        var row = square / n
        var rem = square % n
        var r = n - 1 - row
        var c = if ((row % 2 == 0)) rem else n - 1 - rem
        return intArrayOf(r, c)
    }
}
