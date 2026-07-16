// LeetCode 0399 - Evaluate Division
// https://leetcode.com/problems/evaluate-division/

class Solution {
    func calcEquation(
        _ equations: [[String]],
        _ values: [Double],
        _ queries: [[String]]
    ) -> [Double] {
        var graph: [String: [String: Double]] = [:]

        for index in equations.indices {
            let dividend = equations[index][0]
            let divisor = equations[index][1]
            let value = values[index]
            graph[dividend, default: [:]][divisor] = value
            graph[divisor, default: [:]][dividend] = 1.0 / value
        }

        func dfs(_ start: String, _ end: String, _ visited: inout Set<String>) -> Double {
            guard let startNeighbors = graph[start], graph[end] != nil else {
                return -1.0
            }
            if start == end {
                return 1.0
            }
            visited.insert(start)
            for (neighbor, weight) in startNeighbors where !visited.contains(neighbor) {
                let result = dfs(neighbor, end, &visited)
                if result != -1.0 {
                    return weight * result
                }
            }
            return -1.0
        }

        return queries.map { query in
            var visited: Set<String> = []
            return dfs(query[0], query[1], &visited)
        }
    }
}
