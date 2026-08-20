// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

class Solution {
    func minOperationsMaxProfit(_ customers: [Int], _ boardingCost: Int, _ runningCost: Int) -> Int {
        var waiting = 0, profit = 0, best = 0, answer = 0, rotation = 0
        var i = 0
        while i < customers.count || waiting > 0 {
            if i < customers.count { waiting += customers[i] }
            let boarded = min(4, waiting)
            waiting -= boarded
            rotation += 1
            profit += boarded * boardingCost - runningCost
            if profit > best {
                best = profit
                answer = rotation
            }
            i += 1
        }
        return best > 0 ? answer : -1
    }
}
