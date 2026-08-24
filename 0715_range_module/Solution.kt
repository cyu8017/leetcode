// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

class RangeModule {
    private var intervals = ArrayList<IntArray>()

    fun addRange(left: Int, right: Int) {
        var left = left
        var right = right
        val next = ArrayList<IntArray>()
        var placed = false
        for (iv in intervals) {
            val start = iv[0]
            val end = iv[1]
            if (end < left) next.add(intArrayOf(start, end))
            else if (right < start) {
                if (!placed) {
                    next.add(intArrayOf(left, right))
                    placed = true
                }
                next.add(intArrayOf(start, end))
            } else {
                left = minOf(left, start)
                right = maxOf(right, end)
            }
        }
        if (!placed) next.add(intArrayOf(left, right))
        intervals = next
    }

    fun queryRange(left: Int, right: Int): Boolean {
        for (iv in intervals) {
            if (iv[0] <= left && right <= iv[1]) return true
            if (iv[1] >= right) break
        }
        return false
    }

    fun removeRange(left: Int, right: Int) {
        val next = ArrayList<IntArray>()
        for (iv in intervals) {
            val start = iv[0]
            val end = iv[1]
            if (end <= left || right <= start) next.add(intArrayOf(start, end))
            else {
                if (start < left) next.add(intArrayOf(start, left))
                if (right < end) next.add(intArrayOf(right, end))
            }
        }
        intervals = next
    }
}
