// LeetCode 3661 - Maximum Walls Destroyed by Robots
// https://leetcode.com/problems/maximum-walls-destroyed-by-robots/

class Solution {
    private lateinit var arr: Array<IntArray>
    private lateinit var walls: IntArray
    private lateinit var memo: HashMap<Long, Int>

    private fun lowerBound(a: IntArray, target: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < target) lo = mid + 1
            else hi = mid
        }
        return lo
    }

    private fun dfs(i: Int, j: Int): Int {
        if (i < 0) return 0
        val key = (i.toLong() shl 1) or j.toLong()
        memo[key]?.let { return it }
        var left = arr[i][0] - arr[i][1]
        if (i > 0) left = maxOf(left, arr[i - 1][0] + 1)
        var l = lowerBound(walls, left)
        var r = lowerBound(walls, arr[i][0] + 1)
        var ans = dfs(i - 1, 0) + (r - l)
        var right = arr[i][0] + arr[i][1]
        if (i + 1 < arr.size) {
            right = if (j == 0) minOf(right, arr[i + 1][0] - arr[i + 1][1] - 1)
            else minOf(right, arr[i + 1][0] - 1)
        }
        l = lowerBound(walls, arr[i][0])
        r = lowerBound(walls, right + 1)
        ans = maxOf(ans, dfs(i - 1, 1) + (r - l))
        memo[key] = ans
        return ans
    }

    fun maxWalls(robots: IntArray, distance: IntArray, walls: IntArray): Int {
        val n = robots.size
        arr = Array(n) { IntArray(2) }
        for (i in 0 until n) {
            arr[i][0] = robots[i]
            arr[i][1] = distance[i]
        }
        arr.sortBy { it[0] }
        walls.sort()
        this.walls = walls
        memo = HashMap()
        return dfs(n - 1, 1)
    }
}
