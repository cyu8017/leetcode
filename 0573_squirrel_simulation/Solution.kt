// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/


class Solution {
    fun minDistance(height: Int, width: Int, tree: IntArray, squirrel: IntArray, nuts: Array<IntArray>): Int {
        var total = 0
        var bestSave = Int.MIN_VALUE
        for (nut in nuts) {
            val treeDist = dist(tree, nut)
            val squirrelDist = dist(squirrel, nut)
            total += 2 * treeDist
            bestSave = maxOf(bestSave, treeDist - squirrelDist)
        }
        return total - bestSave
    }

    private fun dist(a: IntArray, b: IntArray): Int =
        kotlin.math.abs(a[0] - b[0]) + kotlin.math.abs(a[1] - b[1])
}
