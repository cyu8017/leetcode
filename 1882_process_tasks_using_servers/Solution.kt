// LeetCode 1882 - Process Tasks Using Servers
// https://leetcode.com/problems/process-tasks-using-servers/

import java.util.PriorityQueue

class Solution {
    fun assignTasks(servers: IntArray, tasks: IntArray): IntArray {
        val available = PriorityQueue(compareBy<IntArray>({ it[0] }, { it[1] }))
        for (index in servers.indices) {
            available.offer(intArrayOf(servers[index], index))
        }
        val busy = PriorityQueue(compareBy<LongArray>({ it[0] }, { it[1] }, { it[2] }))
        val answer = IntArray(tasks.size)
        var time = 0L
        for (moment in tasks.indices) {
            time = maxOf(time, moment.toLong())
            while (busy.isNotEmpty() && busy.peek()[0] <= time) {
                val finished = busy.poll()
                available.offer(intArrayOf(finished[1].toInt(), finished[2].toInt()))
            }
            while (available.isEmpty()) {
                time = busy.peek()[0]
                while (busy.isNotEmpty() && busy.peek()[0] <= time) {
                    val finished = busy.poll()
                    available.offer(intArrayOf(finished[1].toInt(), finished[2].toInt()))
                }
            }
            val server = available.poll()
            busy.offer(longArrayOf(time + tasks[moment], server[0].toLong(), server[1].toLong()))
            answer[moment] = server[1]
        }
        return answer
    }
}
