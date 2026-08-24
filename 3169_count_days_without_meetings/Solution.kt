// LeetCode 3169 - Count Days Without Meetings
// https://leetcode.com/problems/count-days-without-meetings/

class Solution {
    fun countDays(days: Int, meetings: Array<IntArray>): Int {
        meetings, (a, b.sort() -> Integer.compare(a[0], b[0]))
        var last = 0
        var ans = 0
        for (e in meetings) {
            var st = e[0]
            var ed = e[1]
            if (last < st) ans += st - last - 1
            last = maxOf(last, ed)
        }
        ans += days - last
        return ans
    }
}
