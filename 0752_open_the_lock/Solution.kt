// LeetCode 0752 - Open the Lock
// https://leetcode.com/problems/open-the-lock/

class Solution {
    fun openLock(deadends: Array<String>, target: String): Int {
        val dead = deadends.toHashSet()
        if ("0000" in dead) return -1
        val q = ArrayDeque<String>()
        val stepsQ = ArrayDeque<Int>()
        val seen = HashSet<String>()
        seen.add("0000")
        q.add("0000")
        stepsQ.add(0)
        while (q.isNotEmpty()) {
            val state = q.removeFirst()
            val steps = stepsQ.removeFirst()
            if (state == target) return steps
            val chars = state.toCharArray()
            for (i in 0 until 4) {
                val digit = chars[i] - '0'
                for (delta in intArrayOf(-1, 1)) {
                    chars[i] = ('0'.code + (digit + delta + 10) % 10).toChar()
                    val nxt = String(chars)
                    chars[i] = ('0'.code + digit).toChar()
                    if (seen.add(nxt) && nxt !in dead) {
                        q.add(nxt)
                        stepsQ.add(steps + 1)
                    }
                }
            }
        }
        return -1
    }
}
