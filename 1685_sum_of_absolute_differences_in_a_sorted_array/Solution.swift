// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

class Solution {
    func getSumAbsoluteDifferences(_ nums: [Int]) -> [Int] {
        let total = nums.reduce(0, +)
        var left = 0
        let n = nums.count
        var ans = [Int]()
        for i in 0..<n {
            let x = nums[i]
            ans.append(x * i - left + (total - left - x) - x * (n - i - 1))
            left += x
        }
        return ans
    }
}
