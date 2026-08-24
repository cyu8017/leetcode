// LeetCode 3037 - Find Pattern in Infinite Stream II
// https://leetcode.com/problems/find-pattern-in-infinite-stream-ii/

class InfiniteStream(private val bits: IntArray) {
    private var i = 0
    fun next(): Int = bits[i++]
}

class Solution {
    private fun getLPS(pattern: IntArray): IntArray {
        val n = pattern.size
        val lps = IntArray(n)
        var j = 0
        for (i in 1 until n) {
            while (j > 0 && pattern[j] != pattern[i]) j = lps[j - 1]
            if (pattern[i] == pattern[j]) {
                j++
                lps[i] = j
            }
        }
        return lps
    }

    fun findPattern(stream: InfiniteStream, pattern: IntArray): Int {
        val lps = getLPS(pattern)
        var i = 0
        var j = 0
        var bit = 0
        var readNext = false
        while (true) {
            if (!readNext) {
                bit = stream.next()
                readNext = true
            }
            if (bit == pattern[j]) {
                i++
                readNext = false
                j++
                if (j == pattern.size) return i - j
            } else if (j > 0) {
                j = lps[j - 1]
            } else {
                i++
                readNext = false
            }
        }
    }
}
