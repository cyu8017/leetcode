// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

class Solution {
    func minImpossibleOR(_ nums: [Int]) -> Int {
        let set = Set(nums)
        var x = 1
        while set.contains(x) { x <<= 1 }
        return x
    }
}
