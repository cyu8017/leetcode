// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/


class Solution {
    fun exclusiveTime(n: Int, logs: List<String>): IntArray {
        val result = IntArray(n)
        val stack = ArrayDeque<Int>()
        var prev = 0
        for (log in logs) {
            val parts = log.split(':')
            val id = parts[0].toInt()
            val type = parts[1]
            val time = parts[2].toInt()
            if (type == "start") {
                if (stack.isNotEmpty()) result[stack.last()] += time - prev
                stack.addLast(id)
                prev = time
            } else {
                result[stack.removeLast()] += time - prev + 1
                prev = time + 1
            }
        }
        return result
    }
}
