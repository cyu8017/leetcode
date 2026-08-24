// LeetCode 2057 - Smallest Index With Equal Value
// https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution {
    func smallestEqual(_ nums: [Int]) -> Int {
        for i in 0..<nums.count where i % 10 == nums[i] { return i }
        return -1
    }
}
