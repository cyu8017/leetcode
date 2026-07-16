// LeetCode 0360 - Sort Transformed Array
// https://leetcode.com/problems/sort-transformed-array/

class Solution {
    func sortTransformedArray(_ nums: [Int], _ a: Int, _ b: Int, _ c: Int) -> [Int] {
        func transform(_ value: Int) -> Int {
            a * value * value + b * value + c
        }

        var left = 0
        var right = nums.count - 1
        var result = Array(repeating: 0, count: nums.count)
        var index = a > 0 ? nums.count - 1 : 0
        let step = a > 0 ? -1 : 1

        while left <= right {
            let leftValue = transform(nums[left])
            let rightValue = transform(nums[right])

            if a > 0 {
                if leftValue > rightValue {
                    result[index] = leftValue
                    left += 1
                } else {
                    result[index] = rightValue
                    right -= 1
                }
            } else if leftValue < rightValue {
                result[index] = leftValue
                left += 1
            } else {
                result[index] = rightValue
                right -= 1
            }

            index += step
        }

        return result
    }
}
