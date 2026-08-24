// LeetCode 0635 - Design Log Storage System
// https://leetcode.com/problems/design-log-storage-system/


class LogSystem {
    private val logs = ArrayList<Pair<Int, String>>()
    private val indices = mapOf(
        "Year" to 4, "Month" to 7, "Day" to 10,
        "Hour" to 13, "Minute" to 16, "Second" to 19
    )

    fun put(id: Int, timestamp: String) {
        logs.add(id to timestamp)
    }

    fun retrieve(start: String, end: String, granularity: String): List<Int> {
        val idx = indices[granularity]!!
        val s = start.substring(0, idx)
        val e = end.substring(0, idx)
        return logs.filter { it.second.substring(0, idx) in s..e }.map { it.first }
    }
}
