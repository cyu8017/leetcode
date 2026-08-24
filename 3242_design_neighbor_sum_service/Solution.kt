// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

class NeighborSum(private val grid: Array<IntArray>) {
    private val d = HashMap<Int, IntArray>()
    private val dirs = arrayOf(
        intArrayOf(-1, 0, 1, 0, -1),
        intArrayOf(-1, 1, 1, -1, -1)
    )

    init {
        for (i in grid.indices) {
            for (j in grid[i].indices) {
                d[grid[i][j]] = intArrayOf(i, j)
            }
        }
    }

    private fun cal(value: Int, k: Int): Int {
        val p = d[value]!!
        var s = 0
        for (q in 0 until 4) {
            val x = p[0] + dirs[k][q]
            val y = p[1] + dirs[k][q + 1]
            if (x in grid.indices && y in grid[0].indices) {
                s += grid[x][y]
            }
        }
        return s
    }

    fun adjacentSum(value: Int): Int = cal(value, 0)

    fun diagonalSum(value: Int): Int = cal(value, 1)
}
