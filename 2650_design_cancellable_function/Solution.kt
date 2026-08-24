
// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/

class Solution {
    fun cancellable(generator: () -> Int): Array<Any> {
        var cancelled = false
        var done = false
        var result = 0
        val cancel: () -> Unit = { cancelled = true }
        val run: () -> Int = {
            if (!done) {
                result = generator()
                done = true
            }
            result
        }
        return arrayOf(cancel, run, cancelled)
    }
}
