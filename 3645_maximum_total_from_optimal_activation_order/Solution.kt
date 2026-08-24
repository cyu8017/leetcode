// LeetCode 3645 - Maximum Total from Optimal Activation Order
// https://leetcode.com/problems/maximum-total-from-optimal-activation-order/

class Solution {
    fun maxTotal(value: IntArray, limit: IntArray): Long {
        val g = HashMap<Int, ArrayList<Int>>()
        for (i in value.indices) {
            g.getOrPut(limit[i]) { ArrayList() }.add(value[i])
        }
        var ans = 0L
        for ((lim, vs) in g) {
            vs.sortDescending()
            for (i in 0 until minOf(lim, vs.size)) ans += vs[i]
        }
        return ans
    }
}
