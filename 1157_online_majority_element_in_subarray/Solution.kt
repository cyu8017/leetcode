// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

class MajorityChecker(arr: IntArray) {
    private val arr = arr
    private val pos = mutableMapOf<Int, MutableList<Int>>()

    init {
        for (i in arr.indices) {
            pos.getOrPut(arr[i]) { mutableListOf() }.add(i)
        }
    }

    fun query(left: Int, right: Int, threshold: Int): Int {
        var candidate = 0
        var count = 0
        for (i in left..right) {
            if (count == 0) candidate = arr[i]
            count += if (arr[i] == candidate) 1 else -1
        }
        val locs = pos[candidate] ?: return -1
        val freq = upperBound(locs, right) - lowerBound(locs, left)
        return if (freq >= threshold) candidate else -1
    }

    private fun lowerBound(a: List<Int>, t: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < t) lo = mid + 1 else hi = mid
        }
        return lo
    }

    private fun upperBound(a: List<Int>, t: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] <= t) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
