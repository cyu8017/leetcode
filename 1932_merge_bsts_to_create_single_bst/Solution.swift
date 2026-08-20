// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

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
    func canMerge(_ trees: [TreeNode?]) -> TreeNode? {
        let trees = trees.compactMap { $0 }
        var valueToRoot: [Int: TreeNode] = [:]
        var count: [Int: Int] = [:]
        for tree in trees {
            valueToRoot[tree.val] = tree
            count[tree.val, default: 0] += 1
            if let left = tree.left { count[left.val, default: 0] += 1 }
            if let right = tree.right { count[right.val, default: 0] += 1 }
        }
        let roots = trees.filter { count[$0.val] == 1 }
        guard roots.count == 1 else { return nil }
        let root = roots[0]
        valueToRoot.removeValue(forKey: root.val)

        func merge(_ node: TreeNode?) -> Bool {
            guard let node = node else { return true }
            if let left = node.left, let next = valueToRoot.removeValue(forKey: left.val) {
                node.left = next
            }
            if let right = node.right, let next = valueToRoot.removeValue(forKey: right.val) {
                node.right = next
            }
            return merge(node.left) && merge(node.right)
        }
        if !merge(root) || !valueToRoot.isEmpty { return nil }

        func isValidBST(_ node: TreeNode?, _ lo: Int, _ hi: Int) -> Bool {
            guard let node = node else { return true }
            if !(lo < node.val && node.val < hi) { return false }
            return isValidBST(node.left, lo, node.val) && isValidBST(node.right, node.val, hi)
        }
        return isValidBST(root, Int.min, Int.max) ? root : nil
    }
}
