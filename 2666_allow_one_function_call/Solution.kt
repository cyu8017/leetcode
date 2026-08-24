// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

class Solution {
    fun once(fn: (Int) -> Int): (Int) -> Int? {
        var called = false
        var res = 0
        return { arg ->
            if (called) null
            else {
                called = true
                res = fn(arg)
                res
            }
        }
    }
}
