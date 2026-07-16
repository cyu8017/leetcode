// LeetCode 0207 - Course Schedule
// https://leetcode.com/problems/course-schedule/

class Solution {
    func canFinish(_ numCourses: Int, _ prerequisites: [[Int]]) -> Bool {
        var graph = Array(repeating: [Int](), count: numCourses)
        var indegree = Array(repeating: 0, count: numCourses)
        for pair in prerequisites {
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
        }
        var queue = (0..<numCourses).filter { indegree[$0] == 0 }
        var index = 0
        while index < queue.count {
            let course = queue[index]
            index += 1
            for next in graph[course] {
                indegree[next] -= 1
                if indegree[next] == 0 { queue.append(next) }
            }
        }
        return queue.count == numCourses
    }
}