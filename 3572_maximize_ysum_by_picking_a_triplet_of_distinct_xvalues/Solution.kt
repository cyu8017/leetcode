// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

class Solution {
    fun maxSumDistinctTriplet(x: IntArray, y: IntArray): Int {
        val n = x.size
        val arr = Array(n) { IntArray(2) }
        for (i in 0 until n) arr[i] = intArrayOf(x[i], y[i])
        arr.sortByDescending { it[1] }
        var ans = 0
        val vis = HashSet<Int>()
        for (i in 0 until n) {
            val a = arr[i][0]
            val b = arr[i][1]
            if (a !in vis) {
                vis.add(a)
                ans += b
                if (vis.size == 3) return ans
            }
        }
        return -1
    }
}
