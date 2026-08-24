// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

class Solution {
    fun slidingPuzzle(board: Array<IntArray>): Int {
        val start = StringBuilder()
        for (row in board) for (cell in row) start.append(cell)
        val target = "123450"
        val neighbors = arrayOf(
            intArrayOf(1, 3), intArrayOf(0, 2, 4), intArrayOf(1, 5),
            intArrayOf(0, 4), intArrayOf(1, 3, 5), intArrayOf(2, 4)
        )
        val q = ArrayDeque<String>()
        val stepsQ = ArrayDeque<Int>()
        val seen = HashSet<String>()
        val startStr = start.toString()
        seen.add(startStr)
        q.add(startStr)
        stepsQ.add(0)
        while (q.isNotEmpty()) {
            val state = q.removeFirst()
            val steps = stepsQ.removeFirst()
            if (state == target) return steps
            val zero = state.indexOf('0')
            for (nei in neighbors[zero]) {
                val nxt = state.toCharArray()
                val tmp = nxt[zero]
                nxt[zero] = nxt[nei]
                nxt[nei] = tmp
                val ns = String(nxt)
                if (seen.add(ns)) {
                    q.add(ns)
                    stepsQ.add(steps + 1)
                }
            }
        }
        return -1
    }
}
