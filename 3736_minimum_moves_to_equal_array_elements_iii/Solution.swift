// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution {
    func minMoves(_ nums: [Int]) -> Int {
        var mx = 0, s = 0
        for x in nums {
            mx = max(mx, x)
            s += x
        }
        return mx * nums.count - s
    }
}
