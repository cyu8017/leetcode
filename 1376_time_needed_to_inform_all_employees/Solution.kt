// LeetCode 1376 - Time Needed to Inform All Employees
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution {
    fun numOfMinutes(n: Int, headID: Int, manager: IntArray, informTime: IntArray): Int {
        val children = Array(n) { mutableListOf<Int>() }
        for (i in manager.indices) {
            if (manager[i] != -1) children[manager[i]].add(i)
        }
        fun dfs(u: Int): Int {
            var best = 0
            for (v in children[u]) best = maxOf(best, dfs(v))
            return informTime[u] + best
        }
        return dfs(headID)
    }
}
