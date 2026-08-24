// LeetCode 2648 - Generate Fibonacci Sequence
// https://leetcode.com/problems/generate-fibonacci-sequence/

class Solution {
    func fibGenerator() -> () -> Int {
        var a = 0
        var b = 1
        return {
            let v = a
            let na = b
            b = a + b
            a = na
            return v
        }
    }
}
