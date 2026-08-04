// LeetCode 1260 - Shift 2D Grid
// https://leetcode.com/problems/shift-2d-grid/

class Solution {
    fun shiftGrid(grid: Array<IntArray>, k: Int): List<List<Int>> {
        val m = grid.size
        val n = grid[0].size
        var flat = grid.flatMap { it.toList() }.toMutableList()
        val kk = k % flat.size
        if (kk > 0) {
            flat = (flat.takeLast(kk) + flat.dropLast(kk)).toMutableList()
        }
        return List(m) { i -> flat.subList(i * n, (i + 1) * n).toList() }
    }
}
