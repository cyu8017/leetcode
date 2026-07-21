// LeetCode 1860 - Incremental Memory Leak
// https://leetcode.com/problems/incremental-memory-leak/

class Solution {
    fun memLeak(memory1: Int, memory2: Int): IntArray {
        var m1 = memory1
        var m2 = memory2
        var second = 1
        while (m1 >= second || m2 >= second) {
            if (m1 >= m2) m1 -= second else m2 -= second
            second++
        }
        return intArrayOf(second, m1, m2)
    }
}
