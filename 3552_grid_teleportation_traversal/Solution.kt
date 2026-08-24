// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

class Solution {
    fun minMoves(matrix: Array<String>): Int {
        var m = matrix.size
        var n = matrix[0].length
        var g = HashMap<Char, MutableList<IntArray>>()
        var i: Int = 0
while (i < m) {

            var j: Int = 0
while (j < n) {

                if (matrix[i].charAt(j.isLetter()))
                    g.getOrPut(matrix[i][j]) { ArrayList() }.add(intArrayOf(i, j))
        var dirs = {-1, 0, 1, 0, -1}
        val INF = 1  shl  30
        var dist = Array(m) { IntArray(n) }
        for (i in 0 until m) { java.util.dist[i].fill(INF) }
        dist[0][0] = 0
        var q = ArrayDeque<IntArray>()
        q.add(intArrayOf(0, 0))
        while (!q.isEmpty()) {
            var cur = q.pollFirst()
            var i = cur[0]
            var j = cur[1]
            var d = dist[i][j]
            if (i == m - 1 && j == n - 1) return d
            var c = matrix[i][j]
            if (g.containsKey(c)) {
                for (p in g[c]) {
                    var x = p[0]
                    var y = p[1]
                    if (d < dist[x][y]) {
                        dist[x][y] = d
                        q.addFirst(intArrayOf(x, y))
                    }
                }
                g.remove(c)
            }
            for (idx in 0 until 4) {
                var x = i + dirs[idx]
                var y = j + dirs[idx + 1]
                if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] != '#' && d + 1 < dist[x][y]) {
                    dist[x][y] = d + 1
                    q.addLast(intArrayOf(x, y))
                }
            }
        }
        return -1
    }
}
i = i + 1
}
j = j + 1
}
