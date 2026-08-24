// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

class Solution {
    fun survivedRobotsHealths(positions: IntArray, healths: IntArray, directions: String): MutableList<Int> {
        val n = positions.size
        val idx = Array(n) { it }
        idx.sortBy { positions[it] }
        val stack = ArrayList<IntArray>()
        for (i in idx) {
            val cur = intArrayOf(i, healths[i], directions[i].code)
            while (stack.isNotEmpty() && stack[stack.size - 1][2] == 'R'.code && cur[2] == 'L'.code) {
                val top = stack[stack.size - 1]
                if (top[1] == cur[1]) {
                    stack.removeAt(stack.size - 1)
                    cur[1] = 0
                    break
                } else if (top[1] > cur[1]) {
                    top[1]--
                    cur[1] = 0
                    break
                } else {
                    cur[1]--
                    stack.removeAt(stack.size - 1)
                }
            }
            if (cur[1] > 0) stack.add(cur)
        }
        val alive = HashMap<Int, Int>()
        for (r in stack) alive[r[0]] = r[1]
        val ans = ArrayList<Int>()
        for (i in 0 until n) if (alive.containsKey(i)) ans.add(alive[i]!!)
        return ans
    }
}
