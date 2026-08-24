// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/

class Solution {
    fun throttle(fn: () -> Unit, t: Int): () -> Unit {
        var last = System.nanoTime() - 24L * 3600 * 1_000_000_000L
        return {
            val now = System.nanoTime()
            if ((now - last) / 1_000_000L >= t) {
                last = now
                fn()
            }
        }
    }
}
