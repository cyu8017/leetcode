// LeetCode 2011 - Final Value of Variable After Performing Operations
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution {
    func finalValueAfterOperations(_ operations: [String]) -> Int {
        var x = 0
        for op in operations {
            let chars = Array(op)
            if chars[1] == "+" { x += 1 }
            else { x -= 1 }
        }
        return x
    }
}
