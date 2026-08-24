// LeetCode 0582 - Kill Process
// https://leetcode.com/problems/kill-process/


class Solution {
    fun killProcess(pid: List<Int>, ppid: List<Int>, kill: Int): List<Int> {
        val children = HashMap<Int, MutableList<Int>>()
        for (i in pid.indices) {
            children.getOrPut(ppid[i]) { ArrayList() }.add(pid[i])
        }
        val result = ArrayList<Int>()
        val queue = ArrayDeque<Int>()
        queue.add(kill)
        while (queue.isNotEmpty()) {
            val process = queue.removeFirst()
            result.add(process)
            children[process]?.forEach { queue.add(it) }
        }
        return result
    }
}
