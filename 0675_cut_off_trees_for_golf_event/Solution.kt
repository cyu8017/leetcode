// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/


class Solution {
    fun cutOffTree(forest: List<List<Int>>): Int {
        val m = forest.size
        val n = forest[0].size
        val trees = ArrayList<IntArray>()
        for (i in 0 until m) for (j in 0 until n) {
            if (forest[i][j] > 1) trees.add(intArrayOf(forest[i][j], i, j))
        }
        trees.sortBy { it[0] }
        var sr = 0
        var sc = 0
        var total = 0
        for (tree in trees) {
            val steps = bfs(forest, sr, sc, tree[1], tree[2])
            if (steps < 0) return -1
            total += steps
            sr = tree[1]
            sc = tree[2]
        }
        return total
    }

    private fun bfs(forest: List<List<Int>>, sr: Int, sc: Int, tr: Int, tc: Int): Int {
        if (sr == tr && sc == tc) return 0
        val m = forest.size
        val n = forest[0].size
        val visited = Array(m) { BooleanArray(n) }
        val queue = ArrayDeque<IntArray>()
        queue.add(intArrayOf(sr, sc, 0))
        visited[sr][sc] = true
        val dirs = arrayOf(intArrayOf(0, 1), intArrayOf(0, -1), intArrayOf(1, 0), intArrayOf(-1, 0))
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            for (d in dirs) {
                val nr = cur[0] + d[0]
                val nc = cur[1] + d[1]
                if (nr !in 0 until m || nc !in 0 until n || visited[nr][nc] || forest[nr][nc] == 0) continue
                if (nr == tr && nc == tc) return cur[2] + 1
                visited[nr][nc] = true
                queue.add(intArrayOf(nr, nc, cur[2] + 1))
            }
        }
        return -1
    }
}
