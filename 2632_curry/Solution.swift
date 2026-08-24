// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

class Solution {
    func curry(_ fn: @escaping ([Int]) -> Int, _ arity: Int) -> ([Int]) -> Int {
        { args in fn(args) }
    }
}
