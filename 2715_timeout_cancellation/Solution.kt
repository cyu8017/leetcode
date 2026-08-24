// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/

class Solution {
    fun cancellable(fn: () -> Int, t: Int): Array<Any?> {
        var cancelled = false
        val cancel: () -> Unit = { cancelled = true }
        val result: () -> Int? = {
            if (cancelled) null else fn()
        }
        return arrayOf(cancel, result)
    }
}
