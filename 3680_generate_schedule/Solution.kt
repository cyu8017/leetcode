// LeetCode 3680 - Generate Schedule
// https://leetcode.com/problems/generate-schedule/

class Solution {
    private lateinit var matches: ArrayList<IntArray>
    private lateinit var used: BooleanArray
    private lateinit var sched: ArrayList<IntArray>
    private var last0 = -1
    private var last1 = -1

    private fun dfs(): Boolean {
        if (sched.size == matches.size) return true
        for (i in matches.indices) {
            if (used[i]) continue
            val m = matches[i]
            if (m[0] == last0 || m[0] == last1 || m[1] == last0 || m[1] == last1) continue
            used[i] = true
            sched.add(m)
            val p0 = last0
            val p1 = last1
            last0 = m[0]
            last1 = m[1]
            if (dfs()) return true
            last0 = p0
            last1 = p1
            sched.removeAt(sched.size - 1)
            used[i] = false
        }
        return false
    }

    fun generateSchedule(n: Int): Array<IntArray> {
        if (n < 5) return emptyArray()
        matches = ArrayList()
        for (i in 0 until n) {
            for (j in 0 until n) {
                if (i != j) matches.add(intArrayOf(i, j))
            }
        }
        used = BooleanArray(matches.size)
        sched = ArrayList()
        last0 = -1
        last1 = -1
        if (dfs()) return sched.toTypedArray()
        return emptyArray()
    }
}
