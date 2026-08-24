// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

class Solution {
    func maximumTotalSum(_ maximumHeight: [Int]) -> Int {
        let heights = maximumHeight.sorted(by: >)
        var ans = 0
        var prev = Int.max
        for h in heights {
            var cur = h
            if cur >= prev { cur = prev - 1 }
            if cur <= 0 { return -1 }
            ans += cur
            prev = cur
        }
        return ans
    }
}
