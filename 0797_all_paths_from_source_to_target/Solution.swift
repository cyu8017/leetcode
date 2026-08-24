// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution {
    func allPathsSourceTarget(_ graph: [[Int]]) -> [[Int]] {
        let target = graph.count - 1
        var answer = [[Int]]()
        var path = [0]
        func dfs(_ node: Int) {
            if node == target {
                answer.append(path)
                return
            }
            for nei in graph[node] {
                path.append(nei)
                dfs(nei)
                path.removeLast()
            }
        }
        dfs(0)
        return answer
    }
}
