// LeetCode 3975 - Filter Occupied Intervals
// https://leetcode.com/problems/filter-occupied-intervals/

class Solution {
    fun filterOccupiedIntervals(occupiedIntervals: Array<IntArray>, freeStart: Int, freeEnd: Int): Array<IntArray> {
        occupiedIntervals.sortBy { it[0] }
        val busy = ArrayList<IntArray>()
        busy.add(intArrayOf(occupiedIntervals[0][0], occupiedIntervals[0][1]))
        for (i in 1 until occupiedIntervals.size) {
            val cur = occupiedIntervals[i]
            val last = busy[busy.size - 1]
            if (last[1] + 1 < cur[0]) busy.add(intArrayOf(cur[0], cur[1]))
            else if (cur[1] > last[1]) last[1] = cur[1]
        }
        val ans = ArrayList<IntArray>()
        for (it in busy) {
            val s = it[0]
            val e = it[1]
            if (e < freeStart || s > freeEnd) ans.add(intArrayOf(s, e))
            else {
                if (s < freeStart) ans.add(intArrayOf(s, freeStart - 1))
                if (e > freeEnd) ans.add(intArrayOf(freeEnd + 1, e))
            }
        }
        return ans.toTypedArray()
    }
}
