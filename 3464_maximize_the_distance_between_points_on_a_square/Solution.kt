// LeetCode 3464 - Maximize the Distance Between Points on a Square
// https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/

class Solution {
    private fun canPlace(arr: IntArray, perim: Int, k: Int, mid: Int): Boolean {
        val n = arr.size
        for (s in 0 until n) {
            var cnt = 1
            var last = arr[s]
            var idx = s
            while (cnt < k) {
                val target = last + mid
                var found = false
                for (step in 1 until n) {
                    val ni = (idx + step) % n
                    val v = arr[ni]
                    val add = if (ni <= idx) perim else 0
                    if (v + add >= target) {
                        last = v + add
                        idx = ni
                        cnt++
                        found = true
                        break
                    }
                }
                if (!found) break
            }
            if (cnt == k && last - arr[s] <= perim - mid) return true
        }
        return false
    }

    fun maxDistance(side: Int, points: Array<IntArray>, k: Int): Int {
        val arr = IntArray(points.size)
        for (i in points.indices) {
            val x = points[i][0]
            val y = points[i][1]
            val d = when {
                y == 0 -> x
                x == side -> side + y
                y == side -> 2 * side + (side - x)
                else -> 3 * side + (side - y)
            }
            arr[i] = d
        }
        arr.sort()
        val perim = 4 * side
        var lo = 0
        var hi = 2 * side
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (canPlace(arr, perim, k, mid)) lo = mid else hi = mid - 1
        }
        return lo
    }
}
