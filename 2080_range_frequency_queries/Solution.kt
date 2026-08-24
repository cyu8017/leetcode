// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

class RangeFreqQuery {
    private val pos = HashMap<Int, MutableList<Int>>()

    constructor(arr: IntArray) {
        for (i in arr.indices) {
            pos.getOrPut(arr[i]) { mutableListOf() }.add(i)
        }
    }

    fun query(left: Int, right: Int, value: Int): Int {
        val p = pos[value] ?: return 0
        return upper(p, right) - lower(p, left)
    }

    private fun lower(p: MutableList<Int>, x: Int): Int {
        var lo = 0
        var hi = p.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (p[mid] < x) lo = mid + 1
            else hi = mid
        }
        return lo
    }

    private fun upper(p: MutableList<Int>, x: Int): Int {
        var lo = 0
        var hi = p.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (p[mid] <= x) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
