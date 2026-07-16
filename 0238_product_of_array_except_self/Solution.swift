// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

class Solution {
    func productExceptSelf(_ nums: [Int]) -> [Int] {
        let length = nums.count
        var result = Array(repeating: 1, count: length)
        var prefix = 1
        for index in 0..<length {
            result[index] = prefix
            prefix *= nums[index]
        }
        var suffix = 1
        for index in stride(from: length - 1, through: 0, by: -1) {
            result[index] *= suffix
            suffix *= nums[index]
        }
        return result
    }
}
