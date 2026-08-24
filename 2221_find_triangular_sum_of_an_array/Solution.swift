// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution {
    func triangularSum(_ nums: [Int]) -> Int {
        var nums = nums
        while nums.count > 1 {
            var next = [Int](repeating: 0, count: nums.count - 1)
            for i in 0..<next.count {
                next[i] = (nums[i] + nums[i + 1]) % 10
            }
            nums = next
        }
        return nums[0]
    }
}
