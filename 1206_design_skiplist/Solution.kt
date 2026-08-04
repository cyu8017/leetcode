// LeetCode 1206 - Design Skiplist
// https://leetcode.com/problems/design-skiplist/

class Skiplist {
    private val values = mutableListOf<Int>()

    fun search(target: Int): Boolean {
        var lo = 0
        var hi = values.size - 1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            when {
                values[mid] == target -> return true
                values[mid] < target -> lo = mid + 1
                else -> hi = mid - 1
            }
        }
        return false
    }

    fun add(num: Int) {
        var lo = 0
        var hi = values.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (values[mid] < num) lo = mid + 1 else hi = mid
        }
        values.add(lo, num)
    }

    fun erase(num: Int): Boolean {
        var lo = 0
        var hi = values.size - 1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            when {
                values[mid] == num -> {
                    values.removeAt(mid)
                    return true
                }
                values[mid] < num -> lo = mid + 1
                else -> hi = mid - 1
            }
        }
        return false
    }
}
