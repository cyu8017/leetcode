// LeetCode 0732 - My Calendar III
// https://leetcode.com/problems/my-calendar-iii/

class MyCalendarThree {
    private val delta = sortedMapOf<Int, Int>()

    fun book(startTime: Int, endTime: Int): Int {
        delta[startTime] = delta.getOrDefault(startTime, 0) + 1
        delta[endTime] = delta.getOrDefault(endTime, 0) - 1
        var current = 0
        var best = 0
        for (change in delta.values) {
            current += change
            best = maxOf(best, current)
        }
        return best
    }
}
