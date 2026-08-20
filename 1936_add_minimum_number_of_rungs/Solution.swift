// LeetCode 1936 - Add Minimum Number of Rungs
// https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution {
    func addRungs(_ rungs: [Int], _ dist: Int) -> Int {
        var prev = 0, ans = 0
        for r in rungs {
            let gap = r - prev
            if gap > dist { ans += (gap - 1) / dist }
            prev = r
        }
        return ans
    }
}
