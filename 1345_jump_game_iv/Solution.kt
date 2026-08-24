// LeetCode 1345 - Jump Game IV
// https://leetcode.com/problems/jump-game-iv/

class Solution {
    fun minJumps(arr: IntArray): Int {
        val n = arr.size
        val positions = HashMap<Int, MutableList<Int>>()
        for (i in 0 until n) {
            positions.getOrPut(arr[i]) { mutableListOf() }.add(i)
        }
        val queue = ArrayDeque<Int>()
        val seen = BooleanArray(n)
        queue.add(0)
        seen[0] = true
        var steps = 0
        while (queue.isNotEmpty()) {
            repeat(queue.size) {
                val i = queue.removeFirst()
                if (i == n - 1) return steps
                val neighbors = mutableListOf(i - 1, i + 1)
                positions.remove(arr[i])?.let { neighbors.addAll(it) }
                for (j in neighbors) {
                    if (j in 0 until n && !seen[j]) {
                        seen[j] = true
                        queue.add(j)
                    }
                }
            }
            steps++
        }
        return -1
    }
}
