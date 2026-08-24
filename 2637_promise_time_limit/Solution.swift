// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/

class Solution {
    func timeLimit(_ fn: @escaping () -> Int, _ t: Int) -> () -> Int {
        { fn() }
    }
}
