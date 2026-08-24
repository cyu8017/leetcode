// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

class Solution {
    func minCostSetTime(_ startAt: Int, _ moveCost: Int, _ pushCost: Int, _ targetSeconds: Int) -> Int {
        let mins = targetSeconds / 60, secs = targetSeconds % 60
        var ans = cost(startAt, moveCost, pushCost, mins, secs)
        if mins > 0 { ans = min(ans, cost(startAt, moveCost, pushCost, mins - 1, secs + 60)) }
        return ans
    }

    private func cost(_ startAt: Int, _ moveCost: Int, _ pushCost: Int, _ mins: Int, _ secs: Int) -> Int {
        if mins < 0 || mins > 99 || secs < 0 || secs > 99 { return Int.max / 2 }
        let s: String
        if mins > 0 {
            s = String(mins) + String(secs / 10) + String(secs % 10)
        } else {
            s = String(secs)
        }
        var cur = Character(String(startAt))
        var ans = 0
        for c in s {
            if c != cur { ans += moveCost; cur = c }
            ans += pushCost
        }
        return ans
    }
}
