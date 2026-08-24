// LeetCode 2758 - Next Day
// https://leetcode.com/problems/next-day/
// JS Date stand-in using civil-day arithmetic.

class Solution {
    fun nextDay(date: String): String {
        var parts = date.split("-")
        if (parts.size != 3) return date
        var y = parts[0].toInt()
        var m = parts[1].toInt()
        var d = parts[2].toInt()
        var mdays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
        if (isLeap(y)) mdays[2] = 29
        d++
        if (d > mdays[m]) { d = 1; m++; }
        if (m > 12) { m = 1; y++; }
        return String.format("%04d-%02d-%02d", y, m, d)
    }

    private fun isLeap(yy: Int): Boolean {
        return (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)
    }
}
