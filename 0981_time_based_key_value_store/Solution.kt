// LeetCode 0981 - Time Based Key-Value Store
// https://leetcode.com/problems/time-based-key-value-store/

class TimeMap {
    private val times = HashMap<String, MutableList<Int>>()
    private val vals = HashMap<String, MutableList<String>>()

    fun set(key: String, value: String, timestamp: Int) {
        times.getOrPut(key) { mutableListOf() }.add(timestamp)
        vals.getOrPut(key) { mutableListOf() }.add(value)
    }

    fun get(key: String, timestamp: Int): String {
        val tarr = times[key] ?: return ""
        val varr = vals[key]!!
        var lo = 0
        var hi = tarr.size - 1
        var ans = -1
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (tarr[mid] <= timestamp) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return if (ans < 0) "" else varr[ans]
    }
}
