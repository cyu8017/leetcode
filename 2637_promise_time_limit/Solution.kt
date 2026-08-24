// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

class Solution {
    fun timeLimit(fn: () -> Int, t: Int): () -> Int = { fn() }
}
