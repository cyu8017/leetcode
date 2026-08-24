// LeetCode 3288 - Length of the Longest Increasing Path
// https://leetcode.com/problems/length-of-the-longest-increasing-path/

class Solution {
    private fun lis(a: List<Int>): Int {
        val tails = ArrayList<Int>()
        for (x in a) {
            var lo = 0
            var hi = tails.size
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (tails[mid] < x) lo = mid + 1
                else hi = mid
            }
            if (lo == tails.size) tails.add(x)
            else tails[lo] = x
        }
        return tails.size
    }

    fun maxPathLength(coordinates: Array<IntArray>, k: Int): Int {
        val n = coordinates.size
        val arr = Array(n) { IntArray(3) }
        for (i in 0 until n) {
            arr[i][0] = coordinates[i][0]
            arr[i][1] = coordinates[i][1]
            arr[i][2] = i
        }
        arr.sortWith { a, b ->
            if (a[0] == b[0]) b[1].compareTo(a[1]) else a[0].compareTo(b[0])
        }
        val kx = coordinates[k][0]
        val ky = coordinates[k][1]
        val left = ArrayList<Int>()
        val right = ArrayList<Int>()
        for (p in arr) {
            if (p[0] < kx && p[1] < ky) left.add(p[1])
            if (p[0] > kx && p[1] > ky) right.add(p[1])
        }
        return lis(left) + 1 + lis(right)
    }
}
