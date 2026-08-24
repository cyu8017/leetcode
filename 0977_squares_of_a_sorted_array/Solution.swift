// LeetCode 0977 - Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution {
    func sortedSquares(_ nums: [Int]) -> [Int] {
        let n = nums.count
        var ans = Array(repeating: 0, count: n)
        var i = 0, j = n - 1
        for k in stride(from: n - 1, through: 0, by: -1) {
            if abs(nums[i]) > abs(nums[j]) {
                ans[k] = nums[i] * nums[i]
                i += 1
            } else {
                ans[k] = nums[j] * nums[j]
                j -= 1
            }
        }
        return ans
    }
}
