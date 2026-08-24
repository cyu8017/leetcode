// LeetCode 0946 - Validate Stack Sequences
// https://leetcode.com/problems/validate-stack-sequences/

class Solution {
    func validateStackSequences(_ pushed: [Int], _ popped: [Int]) -> Bool {
        var stack = [Int]()
        var j = 0
        for x in pushed {
            stack.append(x)
            while !stack.isEmpty && stack.last! == popped[j] {
                stack.removeLast()
                j += 1
            }
        }
        return stack.isEmpty
    }
}
