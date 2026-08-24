// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

class Solution {
    func sortByAbsoluteValue(_ nums: [Int]) -> [Int] {
        return nums.sorted { abs($0) < abs($1) }
    }
}
