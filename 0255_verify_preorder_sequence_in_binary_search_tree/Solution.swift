// LeetCode 0255 - Verify Preorder Sequence in Binary Search Tree
// https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

class Solution {
    func verifyPreorder(_ preorder: [Int]) -> Bool {
        var low = Int.min
        var stack: [Int] = []

        for value in preorder {
            if value < low {
                return false
            }
            while let last = stack.last, last < value {
                low = stack.removeLast()
            }
            stack.append(value)
        }

        return true
    }
}
