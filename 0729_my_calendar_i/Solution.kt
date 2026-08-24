// LeetCode 0729 - My Calendar I
// https://leetcode.com/problems/my-calendar-i/

class MyCalendar {
    private val bookings = ArrayList<IntArray>()

    fun book(startTime: Int, endTime: Int): Boolean {
        for (b in bookings) {
            if (b[0] < endTime && startTime < b[1]) return false
        }
        bookings.add(intArrayOf(startTime, endTime))
        return true
    }
}
