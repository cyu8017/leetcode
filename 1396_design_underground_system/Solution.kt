// LeetCode 1396 - Design Underground System
// https://leetcode.com/problems/design-underground-system/

class UndergroundSystem {
    private val checkIns = HashMap<Int, Pair<String, Int>>()
    private val stats = HashMap<Pair<String, String>, LongArray>()

    fun checkIn(id: Int, stationName: String, t: Int) {
        checkIns[id] = stationName to t
    }

    fun checkOut(id: Int, stationName: String, t: Int) {
        val (start, begin) = checkIns.remove(id)!!
        val key = start to stationName
        val cur = stats.getOrPut(key) { longArrayOf(0L, 0L) }
        cur[0] += (t - begin).toLong()
        cur[1] += 1L
    }

    fun getAverageTime(startStation: String, endStation: String): Double {
        val cur = stats[startStation to endStation]!!
        return cur[0].toDouble() / cur[1]
    }
}
