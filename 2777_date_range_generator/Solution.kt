// LeetCode 2777 - Date Range Generator
// https://leetcode.com/problems/date-range-generator/
// JS generator stand-in using civil-day arithmetic.

class Solution {
    fun dateRangeGenerator(start: String, end: String, step: Int): MutableList<String> {
        var sp = start.split("-")
        var ep = end.split("-")
        if (sp.size != 3 || ep.size != 3) return ArrayList()
        var y = sp[0].toInt()
        var m = sp[1].toInt()
        var d = sp[2].toInt()
        var ey = ep[0].toInt()
        var em = ep[1].toInt()
        var ed = ep[2].toInt()
        var ans = ArrayList<String>()
        while (cmp(y, m, d, ey, em, ed)) {
            ans.add(String.format("%04d-%02d-%02d", y, m, d))
            var ymd = addDays(y, m, d, step)
            y = ymd[0]
            m = ymd[1]
            d = ymd[2]
        }
        return ans
    }

    private fun isLeap(yy: Int): Boolean {
        return (yy % 4 == 0 && yy % 100 != 0) || (yy % 400 == 0)
    }

    private fun addDays(yy: Int, mm: Int, dd: Int, days: Int): IntArray {
        var mdays = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
        while (days-- > 0) {
            mdays[2] =if (isLeap(yy)) 29 else 28
            dd++
            if (dd > mdays[mm]) {
                dd = 1
                mm++
            }
            if (mm > 12) {
                mm = 1
                yy++
            }
        }
        return intArrayOf(yy, mm, dd)
    }

    private fun cmp(y: Int, m: Int, d: Int, ey: Int, em: Int, ed: Int): Boolean {
        if (y != ey) return y < ey
        if (m != em) return m < em
        return d <= ed
    }
}
