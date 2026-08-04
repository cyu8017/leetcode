// LeetCode 1405 - Longest Happy String
// https://leetcode.com/problems/longest-happy-string/

import java.util.PriorityQueue

class Solution {
    fun longestDiverseString(a: Int, b: Int, c: Int): String {
        val heap = PriorityQueue<IntArray>(compareByDescending { it[0] })
        if (a > 0) heap.offer(intArrayOf(a, 'a'.code))
        if (b > 0) heap.offer(intArrayOf(b, 'b'.code))
        if (c > 0) heap.offer(intArrayOf(c, 'c'.code))
        val answer = StringBuilder()
        while (heap.isNotEmpty()) {
            val cur = heap.poll()
            val len = answer.length
            if (len >= 2 && answer[len - 1].code == cur[1] && answer[len - 2].code == cur[1]) {
                if (heap.isEmpty()) break
                val next = heap.poll()
                answer.append(next[1].toChar())
                if (--next[0] > 0) heap.offer(next)
                heap.offer(cur)
            } else {
                answer.append(cur[1].toChar())
                if (--cur[0] > 0) heap.offer(cur)
            }
        }
        return answer.toString()
    }
}
