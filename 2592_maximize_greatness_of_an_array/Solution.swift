// LeetCode 2592 - Maximize Greatness of an Array
// https://leetcode.com/problems/maximize-greatness-of-an-array/

class Solution {
    func maximizeGreatness(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var i = 0
        for x in nums where x > nums[i] { i += 1 }
        return i
    }
}
