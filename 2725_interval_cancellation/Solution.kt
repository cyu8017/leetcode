// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/

class Solution {
    fun cancellable(fn: () -> Int, t: Int, times: Int): Array<Any> {
        var cancelled = false
        val results = ArrayList<Int>()
        var i = 0
        while (i < times && !cancelled) {
            results.add(fn())
            i++
        }
        val cancel: () -> Unit = { cancelled = true }
        return arrayOf(cancel, results.toIntArray())
    }
}
