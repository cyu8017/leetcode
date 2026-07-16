// LeetCode 0207 - Course Schedule\n// https://leetcode.com/problems/\n\nimport java.util.ArrayDeque

class Solution {
    fun canFinish(numCourses: Int, prerequisites: Array<IntArray>): Boolean {
        val graph = Array(numCourses) { mutableListOf<Int>() }; val indegree = IntArray(numCourses)
        for ((course, pre) in prerequisites) { graph[pre].add(course); indegree[course]++ }
        val queue = ArrayDeque<Int>()
        for (course in 0 until numCourses) if (indegree[course] == 0) queue.addLast(course)
        var taken = 0
        while (queue.isNotEmpty()) { val course = queue.removeFirst(); taken++; for (next in graph[course]) if (--indegree[next] == 0) queue.addLast(next) }
        return taken == numCourses
    }
}
