// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

class Solution {
    func minCost(_ startPos: [Int], _ homePos: [Int], _ rowCosts: [Int], _ colCosts: [Int]) -> Int {
        var ans = 0
        let sr = startPos[0], sc = startPos[1], hr = homePos[0], hc = homePos[1]
        if sr < hr { for r in (sr + 1)...hr { ans += rowCosts[r] } }
        else if sr > hr { for r in stride(from: sr - 1, through: hr, by: -1) { ans += rowCosts[r] } }
        if sc < hc { for c in (sc + 1)...hc { ans += colCosts[c] } }
        else if sc > hc { for c in stride(from: sc - 1, through: hc, by: -1) { ans += colCosts[c] } }
        return ans
    }
}
