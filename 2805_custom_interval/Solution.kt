// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/
// JS-only problem; C# stand-in returning a cancel flag setter.

class Solution {
    fun customInterval(fn: () -> Unit, delay: Int, period: Int): () -> Unit {
        var cancelled = false
        return { cancelled = true }
    }
}
