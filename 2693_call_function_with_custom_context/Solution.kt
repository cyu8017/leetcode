// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

class Solution {
    fun call(fn: (Int, Int) -> Int, ctx: Int, arg: Int): Int = fn(ctx, arg)
}
