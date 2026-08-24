// LeetCode 2402 - Meeting Rooms III
// https://leetcode.com/problems/meeting-rooms-iii/

import java.util.PriorityQueue

class Solution {
    fun mostBooked(n: Int, meetings: Array<IntArray>): Int {
        meetings.sortBy { it[0] }
        val free = PriorityQueue<Long>()
        for (i in 0 until n) free.offer(i.toLong())
        val busy = PriorityQueue(compareBy<LongArray>({ it[0] }, { it[1] }))
        val cnt = IntArray(n)
        for (m in meetings) {
            val start = m[0].toLong()
            val end = m[1].toLong()
            while (busy.isNotEmpty() && busy.peek()[0] <= start) {
                free.offer(busy.poll()[1])
            }
            val dur = end - start
            val room: Long
            val begin: Long
            if (free.isNotEmpty()) {
                room = free.poll()
                begin = start
            } else {
                val top = busy.poll()
                begin = top[0]
                room = top[1]
            }
            busy.offer(longArrayOf(begin + dur, room))
            cnt[room.toInt()]++
        }
        var ans = 0
        for (i in 1 until n) if (cnt[i] > cnt[ans]) ans = i
        return ans
    }
}
