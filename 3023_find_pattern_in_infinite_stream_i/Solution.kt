// LeetCode 3023 - Find Pattern in Infinite Stream I
// https://leetcode.com/problems/find-pattern-in-infinite-stream-i/

class InfiniteStream(private val bits: IntArray) {
    private var i = 0
    fun next(): Int = bits[i++]
}

class Solution {
    fun findPattern(stream: InfiniteStream, pattern: IntArray): Int {
        var a = 0
        var b = 0
        val m = pattern.size
        val half = m shr 1
        val mask1 = (1 shl half) - 1
        val mask2 = (1 shl (m - half)) - 1
        for (i in 0 until half) a = a or (pattern[i] shl (half - 1 - i))
        for (i in half until m) b = b or (pattern[i] shl (m - 1 - i))
        var x = 0
        var y = 0
        var i = 1
        while (true) {
            var v = stream.next()
            y = y shl 1 or v
            v = (y shr (m - half)) and 1
            y = y and mask2
            x = x shl 1 or v
            x = x and mask1
            if (i >= m && a == x && b == y) return i - m
            i++
        }
    }
}
