// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

class Solution {
    func threeConsecutiveOdds(_ arr: [Int]) -> Bool {
        var run = 0
        for value in arr {
            run = value & 1 == 1 ? run + 1 : 0
            if run == 3 { return true }
        }
        return false
    }
}
