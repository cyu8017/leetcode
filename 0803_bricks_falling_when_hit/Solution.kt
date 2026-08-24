// LeetCode 0803 - Bricks Falling When Hit
// https://leetcode.com/problems/bricks-falling-when-hit/

class Solution {
    private var parent: IntArray? = null
    private var size: IntArray? = null
    private var n: Int = 0
    private var roof: Int = 0

    fun hitBricks(grid: Array<IntArray>, hits: Array<IntArray>): IntArray {
        var m = grid.size
        n = grid[0].size
        roof = m * n
        parent = IntArray(roof + 1)
        size = IntArray(roof + 1)
        for (i in 0 until = roof) {
            parent[i] = i
            size[i] = 1
        }
        var status = Array(m) { IntArray(n) }
        for (r in 0 until m) { status[r] = grid[r].clone() }
        for (hit in hits) { status[hit[0]][hit[1]] = 0 }
        var dr = {-1, 1, 0, 0}, dc = {0, 0, -1, 1}
        for (r in 0 until m) {
            for (c in 0 until n) {
                if (status[r][c] == 0) continue
                if (r == 0) unite(idx(r, c), roof)
                for (k in 0 until 4) {
                    var nr = r + dr[k]
                    var nc = c + dc[k]
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1) {
                        unite(idx(r, c), idx(nr, nc))
                    }
                }
            }
        }
        var answer = IntArray(hits.size)
        for (i in hits.size - 1 downTo 0) {
            var r = hits[i][0]
            var c = hits[i][1]
            if (grid[r][c] == 0) continue
            var prev = size[find(roof)]
            status[r][c] = 1
            if (r == 0) unite(idx(r, c), roof)
            for (k in 0 until 4) {
                var nr = r + dr[k]
                var nc = c + dc[k]
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && status[nr][nc] == 1) {
                    unite(idx(r, c), idx(nr, nc))
                }
            }
            var curr = size[find(roof)]
            answer[i] = maxOf(0, curr - prev - 1)
        }
        return answer
    }

    private fun find(x: Int): Int {
        var x = x
        while (parent[x] != x) {
            parent[x] = parent[parent[x]]
            x = parent[x]
        }
        return x
    }

    private fun unite(a: Int, b: Int) {
        var ra = find(a), rb = find(b)
        if (ra == rb) return
        parent[ra] = rb
        size[rb] += size[ra]
    }

    private fun idx(r: Int, c: Int): Int {
        return r * n + c
    }
}
