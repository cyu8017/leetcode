// LeetCode 0747 - Largest Number At Least Twice of Others
// https://leetcode.com/problems/largest-number-at-least-twice-of-others/

class Solution {
    func dominantIndex(_ nums: [Int]) -> Int {
        var mx = -1, second = -1, idx = -1
        for (i, n) in nums.enumerated() {
            if n > mx { second = mx; mx = n; idx = i }
            else if n > second { second = n }
        }
        return mx >= 2 * second ? idx : -1
    }
}
