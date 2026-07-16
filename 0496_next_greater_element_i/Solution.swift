// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

class Solution {
    func nextGreaterElement(_ nums1: [Int], _ nums2: [Int]) -> [Int] {
        var nextGreater: [Int: Int] = [:]
        var stack: [Int] = []
        for num in nums2 {
            while !stack.isEmpty && stack[stack.count - 1] < num {
                nextGreater[stack.removeLast()] = num
            }
            stack.append(num)
        }
        return nums1.map { nextGreater[$0] ?? -1 }
    }
}
