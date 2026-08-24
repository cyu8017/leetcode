// LeetCode 0991 - Broken Calculator
// https://leetcode.com/problems/broken-calculator/

class Solution {
    func brokenCalc(_ startValue: Int, _ target: Int) -> Int {
        var target = target
        var ans = 0
        while target > startValue {
            if target % 2 == 1 { target += 1 }
            else { target /= 2 }
            ans += 1
        }
        return ans + startValue - target
    }
}
