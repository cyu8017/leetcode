// LeetCode 1462 - Course Schedule IV
// https://leetcode.com/problems/course-schedule-iv/

class Solution {
    func checkIfPrerequisite(_ numCourses: Int, _ prerequisites: [[Int]], _ queries: [[Int]]) -> [Bool] {
        var reach = Array(repeating: Array(repeating: false, count: numCourses), count: numCourses)
        for e in prerequisites { reach[e[0]][e[1]] = true }
        for k in 0..<numCourses {
            for i in 0..<numCourses where reach[i][k] {
                for j in 0..<numCourses { reach[i][j] = reach[i][j] || reach[k][j] }
            }
        }
        return queries.map { reach[$0[0]][$0[1]] }
    }
}
