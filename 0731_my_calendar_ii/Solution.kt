// LeetCode 0731 - My Calendar II
// https://leetcode.com/problems/my-calendar-ii/

class MyCalendarTwo {
    private val booked = ArrayList<IntArray>()
    private val overlaps = ArrayList<IntArray>()

    fun book(startTime: Int, endTime: Int): Boolean {
        for (o in overlaps) {
            if (o[0] < endTime && startTime < o[1]) return false
        }
        for (b in booked) {
            if (b[0] < endTime && startTime < b[1]) {
                overlaps.add(intArrayOf(maxOf(b[0], startTime), minOf(b[1], endTime)))
            }
        }
        booked.add(intArrayOf(startTime, endTime))
        return true
    }
}
