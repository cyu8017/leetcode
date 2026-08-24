// LeetCode 0850 - Rectangle Area II
// https://leetcode.com/problems/rectangle-area-ii/

class Solution {
    fun rectangleArea(rectangles: Array<IntArray>): Int {
        val MOD = 1_000_000_007
        var events = ArrayList<IntArray>()
        for (r in rectangles) {
            events.add(intArrayOf(r[0], 1, r[1], r[3]))
            events.add(intArrayOf(r[2], -1, r[1], r[3]))
        }
        events.sort(Comparator.comparingInt(a -> a[0]))
        var active = ArrayList<IntArray>()
        var area = 0
        var prevX = events[0][0]
        for (e in events) {
            var x = e[0]
            var typ = e[1]
            var y1 = e[2]
            var y2 = e[3]
            area += coveredLength(active) * (x - prevX)
            if (typ == 1) active.add(intArrayOf(y1, y2))
            else {
                for (i in 0 until active.size) {
                    if (active[i][0] == y1 && active[i][1] == y2) {
                        active.remove(i)
                        break
                    }
                }
            }
            prevX = x
        }
        return (area % MOD)
    }

    private fun coveredLength(active: MutableList<IntArray>): Int {
        if (active.isEmpty()) return 0
        var sorted = ArrayList(active)
        sorted.sort(Comparator.comparingInt(a -> a[0]))
        var total = 0, curStart = sorted[0][0], curEnd = sorted[0][1]
        for (i in 1 until sorted.size) {
            var start = sorted[i][0], end = sorted[i][1]
            if (start > curEnd) {
                total += curEnd - curStart
                curStart = start
                curEnd = end
            } else {
                curEnd = maxOf(curEnd, end)
            }
        }
        total += curEnd - curStart
        return total
    }
}
