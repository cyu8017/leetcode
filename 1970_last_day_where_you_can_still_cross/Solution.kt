// LeetCode 1970
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

class Solution {
    fun latestDayToCross(row: Int, col: Int, cells: Array<IntArray>): Int {
        fun can(day: Int): Boolean {
            val blocked = HashSet<Long>()
            for (i in 0 until day) blocked.add((cells[i][0] - 1).toLong() * col + (cells[i][1] - 1))
            val stack = ArrayDeque<IntArray>()
            val seen = HashSet<Long>()
            for (c in 0 until col) {
                val key = 0L * col + c
                if (key !in blocked) {
                    stack.add(intArrayOf(0, c))
                    seen.add(key)
                }
            }
            while (stack.isNotEmpty()) {
                val cur = stack.removeLast()
                val r = cur[0]
                val c = cur[1]
                if (r == row - 1) return true
                for ((nr, nc) in listOf(r - 1 to c, r + 1 to c, r to c - 1, r to c + 1)) {
                    if (nr in 0 until row && nc in 0 until col) {
                        val key = nr.toLong() * col + nc
                        if (key !in blocked && key !in seen) {
                            seen.add(key)
                            stack.add(intArrayOf(nr, nc))
                        }
                    }
                }
            }
            return false
        }
        var lo = 1
        var hi = cells.size
        var ans = 0
        while (lo <= hi) {
            val mid = (lo + hi) / 2
            if (can(mid)) {
                ans = mid
                lo = mid + 1
            } else hi = mid - 1
        }
        return ans
    }
}
