// LeetCode 0681 - Next Closest Time
// https://leetcode.com/problems/next-closest-time/

class Solution {
    fun nextClosestTime(time: String): String {
        val digits = HashSet<Char>()
        digits.add(time[0])
        digits.add(time[1])
        digits.add(time[3])
        digits.add(time[4])
        val start = time.substring(0, 2).toInt() * 60 + time.substring(3, 5).toInt()
        for (delta in 1..(24 * 60)) {
            val mins = (start + delta) % (24 * 60)
            val hh = mins / 60
            val mm = mins % 60
            val c0 = ('0'.code + hh / 10).toChar()
            val c1 = ('0'.code + hh % 10).toChar()
            val c2 = ('0'.code + mm / 10).toChar()
            val c3 = ('0'.code + mm % 10).toChar()
            if (c0 in digits && c1 in digits && c2 in digits && c3 in digits) {
                return "" + c0 + c1 + ":" + c2 + c3
            }
        }
        return time
    }
}
