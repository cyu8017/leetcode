// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution {
    func minMoves(_ nums: [Int]) -> Int {
        let minimum = nums.min() ?? 0
        return nums.reduce(0) { $0 + ($1 - minimum) }
    }
}
