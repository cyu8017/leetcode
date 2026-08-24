// LeetCode 4012 - Count of Unfinished Tasks After Each Shift
// https://leetcode.com/problems/count-of-unfinished-tasks-after-each-shift/

class Solution {
    fun countTasks(tasks: IntArray, shifts: IntArray): IntArray {
        var m = tasks.size
        var n = shifts.size
        var s = LongArray(m + 1)
        for (i in 0 until m) { s[i + 1] = s[i] + tasks[i] }
        var ans = IntArray(n)
        var iIdx = 0
        var cur = 0
        for (j in 0 until n) {
            if (shifts[j] < tasks[iIdx] - cur) {
                cur += shifts[j]
                ans[j] = m - iIdx
            } else {
                var t = shifts[j] - (tasks[iIdx] - cur)
                if (t >= s[m] - s[iIdx + 1]) {
                    iIdx = 0
                    cur = 0
                } else {
                    var l = iIdx + 1
                    var r = m
                    while (l < r) {
                        var mid = (l + r)  shr  1
                        if (t < s[mid + 1] - s[iIdx + 1]) r = mid
                        else l = mid + 1
                    }
                    cur = t - (s[l] - s[iIdx + 1])
                    iIdx = l
                    ans[j] = m - iIdx
                }
            }
        }
        return ans
    }
}
