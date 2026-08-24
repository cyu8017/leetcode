// LeetCode 2876 - Count Visited Nodes in a Directed Graph
// https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/

class Solution {
    private var edges: [Int] = []
    private var ans: [Int] = []
    private var state: [Int] = []
    private var stack: [Int] = []

    func countVisitedNodes(_ edgesList: [Int]) -> [Int] {
        let n = edgesList.count
        edges = edgesList
        ans = Array(repeating: 0, count: n)
        state = Array(repeating: 0, count: n)
        stack = []
        for i in 0..<n where state[i] == 0 {
            dfs(i)
        }
        return ans
    }

    private func dfs(_ u: Int) {
        state[u] = 1
        stack.append(u)
        let v = edges[u]
        if state[v] == 0 {
            dfs(v)
        } else if state[v] == 1 {
            var idx = stack.count - 1
            while stack[idx] != v { idx -= 1 }
            let cyc = stack.count - idx
            for i in idx..<stack.count {
                ans[stack[i]] = cyc
            }
        }
        if ans[u] == 0 { ans[u] = ans[edges[u]] + 1 }
        state[u] = 2
        stack.removeLast()
    }
}
