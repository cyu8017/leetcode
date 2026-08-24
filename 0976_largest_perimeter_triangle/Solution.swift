// LeetCode 0976 - Largest Perimeter Triangle
// https://leetcode.com/problems/largest-perimeter-triangle/

class Solution {
    func largestPerimeter(_ nums: [Int]) -> Int {
        let a = nums.sorted()
        for i in stride(from: a.count - 1, through: 2, by: -1) {
            if a[i] < a[i - 1] + a[i - 2] { return a[i] + a[i - 1] + a[i - 2] }
        }
        return 0
    }
}
