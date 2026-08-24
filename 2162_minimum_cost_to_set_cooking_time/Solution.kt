// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

class Solution {
    fun cost(startAt: Int, moveCost: Int, pushCost: Int, mins: Int, secs: Int): Int {
        if (mins < 0 || mins > 99 || secs < 0 || secs > 99) return Int.MAX_VALUE / 2
        var s: String
        if (mins > 0) s = mins + "" + ('0' + secs / 10) + ('0' + secs % 10)
        else s = Int.toString(secs)
        var cur: Char = ('0' + startAt)
        var ans: Int = 0
        for (i in 0 until s.length) {
            var c: Char = s[i]
            if (c != cur) { ans += moveCost; cur = c; }
            ans += pushCost
        }
        return ans
    }

    fun minCostSetTime(startAt: Int, moveCost: Int, pushCost: Int, targetSeconds: Int): Int {
        var mins: Int = targetSeconds / 60, secs = targetSeconds % 60
        var ans: Int = cost(startAt, moveCost, pushCost, mins, secs)
        if (mins > 0) ans = minOf(ans, cost(startAt, moveCost, pushCost, mins - 1, secs + 60))
        return ans
    }
}
