// LeetCode 0169 - Majority Element
// https://leetcode.com/problems/majority-element/

class Solution {
    func majorityElement(_ nums: [Int]) -> Int {
        var candidate = 0, count = 0
        for number in nums {
            if count == 0 { candidate = number }
            count += number == candidate ? 1 : -1
        }
        return candidate
    }
}