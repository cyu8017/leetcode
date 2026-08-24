// LeetCode 2754 - Bind Function to Context
// https://leetcode.com/problems/bind-function-to-context/

class Solution {
    func bindFunction(_ fn: (Int, [Int]) -> Int, _ ctx: Int) -> ([Int]) -> Int {
        { args in fn(ctx, args) }
    }

    func bindFunction(_ fn: Int, _ args: [Int]) -> Int {
        fn
    }
}
