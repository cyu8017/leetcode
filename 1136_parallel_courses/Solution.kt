// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

class Solution {
    fun minimumSemesters(n: Int, relations: Array<IntArray>): Int {
        val graph = Array(n + 1) { mutableListOf<Int>() }
        val indegree = IntArray(n + 1)
        for (r in relations) {
            graph[r[0]].add(r[1])
            indegree[r[1]]++
        }
        val queue = ArrayDeque<Int>()
        for (i in 1..n) if (indegree[i] == 0) queue.add(i)
        var semesters = 0
        var taken = 0
        while (queue.isNotEmpty()) {
            semesters++
            repeat(queue.size) {
                val course = queue.removeFirst()
                taken++
                for (nxt in graph[course]) {
                    indegree[nxt]--
                    if (indegree[nxt] == 0) queue.add(nxt)
                }
            }
        }
        return if (taken == n) semesters else -1
    }
}
