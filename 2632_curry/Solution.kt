// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

class Solution {
    fun curry(fn: (IntArray) -> Int, arity: Int): (IntArray) -> Int = { args -> fn(args) }
}
