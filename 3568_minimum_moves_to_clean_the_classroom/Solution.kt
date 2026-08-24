// LeetCode 3568 - Minimum Moves to Clean the Classroom
// https://leetcode.com/problems/minimum-moves-to-clean-the-classroom/

class Solution {
    fun minMoves(classroom: Array<String>, energy: Int): Int {
        val m = classroom.size
        val n = classroom[0].length
        val d = Array(m) { IntArray(n) }
        var x = 0
        var y = 0
        var cnt = 0
        for (i in 0 until m) {
            for (j in 0 until n) {
                val c = classroom[i][j]
                if (c == 'S') { x = i; y = j }
                else if (c == 'L') d[i][j] = cnt++
            }
        }
        if (cnt == 0) return 0
        val vis = Array(m) { Array(n) { Array(energy + 1) { BooleanArray(1 shl cnt) } } }
        var q = ArrayList<IntArray>()
        q.add(intArrayOf(x, y, energy, (1 shl cnt) - 1))
        vis[x][y][energy][(1 shl cnt) - 1] = true
        val dirs = intArrayOf(-1, 0, 1, 0, -1)
        var ans = 0
        while (q.isNotEmpty()) {
            val t = q
            q = ArrayList()
            for (s in t) {
                val i = s[0]
                val j = s[1]
                val curEnergy = s[2]
                val mask = s[3]
                if (mask == 0) return ans
                if (curEnergy <= 0) continue
                for (k in 0 until 4) {
                    val nx = i + dirs[k]
                    val ny = j + dirs[k + 1]
                    if (nx in 0 until m && ny in 0 until n && classroom[nx][ny] != 'X') {
                        val nxtEnergy = if (classroom[nx][ny] == 'R') energy else curEnergy - 1
                        var nxtMask = mask
                        if (classroom[nx][ny] == 'L') nxtMask = nxtMask and (1 shl d[nx][ny]).inv()
                        if (!vis[nx][ny][nxtEnergy][nxtMask]) {
                            vis[nx][ny][nxtEnergy][nxtMask] = true
                            q.add(intArrayOf(nx, ny, nxtEnergy, nxtMask))
                        }
                    }
                }
            }
            ans++
        }
        return -1
    }
}
