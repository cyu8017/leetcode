// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val
        self.left = left
        self.right = right
    }
}

class Solution {
    func findDistance(_ root: TreeNode?, _ p: Int, _ q: Int) -> Int {
        var graph: [Int: [Int]] = [:]

        func dfs(_ node: TreeNode?, _ parent: TreeNode?) {
            guard let node = node else {
                return
            }
            if graph[node.val] == nil {
                graph[node.val] = []
            }
            if let parent = parent {
                graph[node.val]!.append(parent.val)
                graph[parent.val]!.append(node.val)
            }
            dfs(node.left, node)
            dfs(node.right, node)
        }

        dfs(root, nil)
        var queue: [(node: Int, dist: Int)] = [(p, 0)]
        var head = 0
        var seen: Set<Int> = [p]
        while head < queue.count {
            let (node, dist) = queue[head]
            head += 1
            if node == q {
                return dist
            }
            for nei in graph[node] ?? [] {
                if seen.insert(nei).inserted {
                    queue.append((nei, dist + 1))
                }
            }
        }
        return -1
    }
}
