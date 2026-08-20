// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution {
    func countSubTrees(_ n: Int, _ edges: [[Int]], _ labels: String) -> [Int] {
        var graph = Array(repeating: [Int](), count: n)
        for e in edges {
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        }
        let labs = Array(labels)
        var answer = Array(repeating: 0, count: n)
        func dfs(_ node: Int, _ parent: Int) -> [Int] {
            var counts = Array(repeating: 0, count: 26)
            let index = Int(labs[node].asciiValue! - Character("a").asciiValue!)
            counts[index] = 1
            for nei in graph[node] where nei != parent {
                let child = dfs(nei, node)
                for i in 0..<26 { counts[i] += child[i] }
            }
            answer[node] = counts[index]
            return counts
        }
        _ = dfs(0, -1)
        return answer
    }
}
