// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

class Solution {
    func nextGreaterElements(_ nums: [Int]) -> [Int] {
        let length = nums.count
        var result = Array(repeating: -1, count: length)
        var stack: [Int] = []

        for index in 0..<(length * 2) {
            while !stack.isEmpty && nums[stack[stack.count - 1]] < nums[index % length] {
                result[stack.removeLast()] = nums[index % length]
            }
            if index < length {
                stack.append(index)
            }
        }
        return result
    }
}
