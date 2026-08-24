// LeetCode 0767 - Reorganize String
// https://leetcode.com/problems/reorganize-string/

import java.util.PriorityQueue

class Solution {
    fun reorganizeString(s: String): String {
        val freq = IntArray(26)
        for (ch in s) freq[ch - 'a']++
        val heap = PriorityQueue(compareByDescending<IntArray> { it[0] })
        for (i in 0 until 26) {
            if (freq[i] > 0) heap.offer(intArrayOf(freq[i], i))
        }
        if (heap.isNotEmpty() && heap.peek()[0] > (s.length + 1) / 2) return ""
        val result = StringBuilder()
        while (heap.size >= 2) {
            val x = heap.poll()
            val y = heap.poll()
            result.append(('a'.code + x[1]).toChar())
            result.append(('a'.code + y[1]).toChar())
            if (--x[0] > 0) heap.offer(x)
            if (--y[0] > 0) heap.offer(y)
        }
        if (heap.isNotEmpty()) result.append(('a'.code + heap.peek()[1]).toChar())
        return result.toString()
    }
}
