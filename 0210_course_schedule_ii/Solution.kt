// LeetCode 0210 - Course Schedule II\n// https://leetcode.com/problems/\n\nimport java.util.ArrayDeque

class Solution {
    fun findOrder(numCourses: Int, prerequisites: Array<IntArray>): IntArray {
        val graph = Array(numCourses) { mutableListOf<Int>() }; val indegree = IntArray(numCourses)
        for ((course, pre) in prerequisites) { graph[pre].add(course); indegree[course]++ }
        val queue = ArrayDeque<Int>()
        for (course in 0 until numCourses) if (indegree[course] == 0) queue.addLast(course)
        val order = IntArray(numCourses); var index = 0
        while (queue.isNotEmpty()) { val course = queue.removeFirst(); order[index++] = course; for (next in graph[course]) if (--indegree[next] == 0) queue.addLast(next) }
        return if (index == numCourses) order else IntArray(0)
    }
}
