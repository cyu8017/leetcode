// LeetCode 1273 - Delete Tree Nodes
// https://leetcode.com/problems/delete-tree-nodes/

class Solution {
    func deleteTreeNodes(_ nodes: Int, _ parent: [Int], _ value: [Int]) -> Int {
        var children = [[Int]](repeating: [], count: nodes)
        for i in 0..<nodes where parent[i] != -1 {
            children[parent[i]].append(i)
        }
        func dfs(_ u: Int) -> (Int, Int) {
            var sum = value[u], cnt = 1
            for v in children[u] {
                let (s, c) = dfs(v)
                sum += s
                cnt += c
            }
            if sum == 0 { return (0, 0) }
            return (sum, cnt)
        }
        return dfs(0).1
    }
}
