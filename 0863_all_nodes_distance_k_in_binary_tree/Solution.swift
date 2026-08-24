// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

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
    func distanceK(_ root: TreeNode?, _ target: TreeNode?, _ k: Int) -> [Int] {
        guard let root = root, let target = target else { return [] }
        var graph = [ObjectIdentifier: [TreeNode]]()
        func build(_ node: TreeNode?, _ parent: TreeNode?) {
            guard let node = node else { return }
            if let parent = parent {
                graph[ObjectIdentifier(node), default: []].append(parent)
                graph[ObjectIdentifier(parent), default: []].append(node)
            }
            build(node.left, node)
            build(node.right, node)
        }
        build(root, nil)
        var queue: [TreeNode] = [target]
        var seen: Set<ObjectIdentifier> = [ObjectIdentifier(target)]
        var dist = 0
        var qi = 0
        while qi < queue.count {
            if dist == k { return queue[qi...].map { $0.val } }
            let size = queue.count - qi
            for _ in 0..<size {
                let node = queue[qi]
                qi += 1
                for nei in graph[ObjectIdentifier(node), default: []] {
                    if seen.insert(ObjectIdentifier(nei)).inserted {
                        queue.append(nei)
                    }
                }
            }
            dist += 1
        }
        return []
    }
}
