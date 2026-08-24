// LeetCode 2148 - Count Elements With Strictly Smaller and Greater Elements
// https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

class Solution {
    func countElements(_ nums: [Int]) -> Int {
        let mn = nums.min()!, mx = nums.max()!
        return nums.filter { $0 > mn && $0 < mx }.count
    }
}
