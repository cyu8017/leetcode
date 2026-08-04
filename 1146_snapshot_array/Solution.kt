// LeetCode 1146 - Snapshot Array
// https://leetcode.com/problems/snapshot-array/

class SnapshotArray(length: Int) {
    private var snapId = 0
    private val data = Array(length) { mutableListOf(intArrayOf(0, 0)) }

    fun set(index: Int, `val`: Int) {
        val hist = data[index]
        val last = hist.last()
        if (last[0] == snapId) last[1] = `val`
        else hist.add(intArrayOf(snapId, `val`))
    }

    fun snap(): Int = snapId++

    fun get(index: Int, snap_id: Int): Int {
        val hist = data[index]
        var lo = 0
        var hi = hist.size - 1
        var ans = 0
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (hist[mid][0] <= snap_id) {
                ans = mid
                lo = mid + 1
            } else hi = mid - 1
        }
        return hist[ans][1]
    }
}
