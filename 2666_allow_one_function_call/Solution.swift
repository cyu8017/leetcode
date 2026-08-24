// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

class Solution {
    func once(_ fn: @escaping (Int) -> Int) -> (Int) -> Int? {
        var called = false
        return { arg in
            if called { return nil }
            called = true
            return fn(arg)
        }
    }
}
