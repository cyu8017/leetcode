// LeetCode 1991 - Find the Middle Index in Array
// https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution {
    func findMiddleIndex(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var left = 0
        for (i, x) in nums.enumerated() {
            if left == total - left - x { return i }
            left += x
        }
        return -1
    }
}
