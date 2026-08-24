// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        let nums = nums.sorted()
        var sum = nums.reduce(0, +)
        for i in stride(from: nums.count - 1, through: 2, by: -1) {
            sum -= nums[i]
            if sum > nums[i] { return sum + nums[i] }
        }
        return -1
    }
}
