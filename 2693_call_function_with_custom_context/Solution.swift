// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/

class Solution {
    func call(_ fn: (Int, Int) -> Int, _ ctx: Int, _ arg: Int) -> Int {
        fn(ctx, arg)
    }
}
