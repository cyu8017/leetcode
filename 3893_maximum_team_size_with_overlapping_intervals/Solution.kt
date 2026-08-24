// LeetCode 3893 - Maximum Team Size With Overlapping Intervals
// https://leetcode.com/problems/maximum-team-size-with-overlapping-intervals/

class Solution {
    fun maximumTeamSize(startTime: IntArray, endTime: IntArray): Int {
        var n = startTime.size
        var st = startTime.clone()
        var en = endTime.clone()
        st.sort()
        en.sort()
        var ans = 0
        for (t in 0 until n) {
            var l = startTime[t]
            var r = endTime[t]
            var i = UpperBound(en, l - 1)
            var j = UpperBound(st, r)
            ans = maxOf(ans, j - i)
        }
        return ans
    }
    fun UpperBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            var mid = (lo + hi) / 2
            if (a[mid] <= x) lo = mid + 1
            else hi = mid
        }
        return lo
    }
}
