// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

class Solution {
    func largestPathValue(_ colors: String, _ edges: [[Int]]) -> Int {
        let n = colors.count
        let colorChars = Array(colors)
        var indegree = Array(repeating: 0, count: n)
        var adjacency = Array(repeating: [Int](), count: n)

        for edge in edges {
            adjacency[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        }

        var queue: [Int] = []
        for node in 0..<n where indegree[node] == 0 {
            queue.append(node)
        }

        var dp = Array(repeating: Array(repeating: 0, count: 26), count: n)
        for node in 0..<n {
            dp[node][Int(colorChars[node].asciiValue! - 97)] = 1
        }

        var processed = 0
        var answer = 0
        var head = 0

        while head < queue.count {
            let node = queue[head]
            head += 1
            processed += 1
            answer = max(answer, dp[node].max() ?? 0)

            for neighbor in adjacency[node] {
                let neighborColor = Int(colorChars[neighbor].asciiValue! - 97)
                for colorIndex in 0..<26 {
                    var candidate = dp[node][colorIndex]
                    if colorIndex == neighborColor {
                        candidate += 1
                    }
                    if candidate > dp[neighbor][colorIndex] {
                        dp[neighbor][colorIndex] = candidate
                    }
                }

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0 {
                    queue.append(neighbor)
                }
            }
        }

        return processed == n ? answer : -1
    }
}
