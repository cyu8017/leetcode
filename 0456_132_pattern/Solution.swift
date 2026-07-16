// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

class Solution {
    func find132pattern(_ nums: [Int]) -> Bool {
        var stack: [Int] = []
        var third = Int.min

        for value in nums.reversed() {
            if value < third {
                return true
            }
            while !stack.isEmpty && value > stack[stack.count - 1] {
                third = stack.removeLast()
            }
            stack.append(value)
        }

        return false
    }
}
