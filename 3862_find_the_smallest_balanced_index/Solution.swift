// LeetCode 3862 - Find The Smallest Balanced Index
// https://leetcode.com/problems/find-the-smallest-balanced-index/

class Solution {
    func smallestBalancedIndex(_ nums: [Int]) -> Int {
        var s = 0, p = 1
        for x in nums { s += x }
        for i in stride(from: nums.count - 1, through: 0, by: -1) {
            s -= nums[i]
            if s == p { return i }
            p *= nums[i]
            if p >= s { break }
        }
        return -1
    }
}
