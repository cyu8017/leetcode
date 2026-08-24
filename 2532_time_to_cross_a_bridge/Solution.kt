// LeetCode 2532 - Time to Cross a Bridge
// https://leetcode.com/problems/time-to-cross-a-bridge/

class Solution {
    private class Worker(val idx: Int, t: IntArray) {
        val leftToRight = t[0]
        val pickOld = t[1]
        val rightToLeft = t[2]
        val putNew = t[3]
        val efficiency = t[0] + t[2]
    }

    fun findCrossingTime(n: Int, k: Int, time: Array<IntArray>): Int {
        val cmp = Comparator<Worker> { a, b ->
            if (a.efficiency != b.efficiency) b.efficiency.compareTo(a.efficiency)
            else b.idx.compareTo(a.idx)
        }
        val left = java.util.PriorityQueue(cmp)
        val right = java.util.PriorityQueue(cmp)
        val ws = Array(k) { Worker(it, time[it]) }
        for (w in ws) left.offer(w)
        val events = java.util.PriorityQueue<LongArray>(compareBy { it[0] })
        var cur = 0L
        var bridgeFree = 0L
        var remain = n
        var done = 0
        while (done < n) {
            while (events.isNotEmpty() && events.peek()[0] <= cur) {
                val e = events.poll()
                val w = ws[e[2].toInt()]
                if (e[1].toInt() == 0) left.offer(w) else right.offer(w)
            }
            if (cur < bridgeFree) {
                cur = bridgeFree
                continue
            }
            if (right.isNotEmpty()) {
                val w = right.poll()
                cur += w.rightToLeft
                bridgeFree = cur
                events.offer(longArrayOf(cur + w.putNew, 0, w.idx.toLong()))
                done += 1
                continue
            }
            if (left.isNotEmpty() && remain > 0) {
                val w = left.poll()
                cur += w.leftToRight
                bridgeFree = cur
                remain -= 1
                events.offer(longArrayOf(cur + w.pickOld, 1, w.idx.toLong()))
                continue
            }
            if (events.isEmpty()) break
            cur = events.peek()[0]
        }
        return cur.toInt()
    }
}
