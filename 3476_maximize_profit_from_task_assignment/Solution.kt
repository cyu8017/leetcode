// LeetCode 3476 - Maximize Profit from Task Assignment
// https://leetcode.com/problems/maximize-profit-from-task-assignment/

class Solution {
    fun maxProfit(workers: IntArray, tasks: Array<IntArray>): Long {
        workers.sort()
        tasks.sortBy { it[0] }
        var ans = 0L
        val used = BooleanArray(tasks.size)
        for (w in workers) {
            var best = -1
            var bi = -1
            for (i in tasks.indices) {
                if (used[i]) continue
                if (tasks[i][0] > w) break
                if (tasks[i][1] > best) {
                    best = tasks[i][1]
                    bi = i
                }
            }
            if (bi >= 0) {
                used[bi] = true
                ans += best.toLong()
            }
        }
        return ans
    }
}
