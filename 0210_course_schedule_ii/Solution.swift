// LeetCode 0210 - Course Schedule II
// https://leetcode.com/problems/course-schedule-ii/

class Solution {
    func findOrder(_ numCourses: Int, _ prerequisites: [[Int]]) -> [Int] {
        var graph = Array(repeating: [Int](), count: numCourses)
        var indegree = Array(repeating: 0, count: numCourses)
        for pair in prerequisites {
            graph[pair[1]].append(pair[0])
            indegree[pair[0]] += 1
        }
        var order = (0..<numCourses).filter { indegree[$0] == 0 }
        var index = 0
        while index < order.count {
            let course = order[index]
            index += 1
            for next in graph[course] {
                indegree[next] -= 1
                if indegree[next] == 0 { order.append(next) }
            }
        }
        return order.count == numCourses ? order : []
    }
}