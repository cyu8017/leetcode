// LeetCode 1136 - Parallel Courses
// https://leetcode.com/problems/parallel-courses/

class Solution {
    func minimumSemesters(_ n: Int, _ relations: [[Int]]) -> Int {
        var graph = [[Int]](repeating: [], count: n + 1)
        var indegree = [Int](repeating: 0, count: n + 1)
        for r in relations {
            graph[r[0]].append(r[1])
            indegree[r[1]] += 1
        }
        var queue: [Int] = []
        for i in 1...n where indegree[i] == 0 { queue.append(i) }
        var semesters = 0, taken = 0, qi = 0
        while qi < queue.count {
            semesters += 1
            let size = queue.count - qi
            for _ in 0..<size {
                let course = queue[qi]; qi += 1
                taken += 1
                for nxt in graph[course] {
                    indegree[nxt] -= 1
                    if indegree[nxt] == 0 { queue.append(nxt) }
                }
            }
        }
        return taken == n ? semesters : -1
    }
}
