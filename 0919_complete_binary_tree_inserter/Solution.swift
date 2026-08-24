// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

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

class CBTInserter {
    private let root: TreeNode
    private var parents = [TreeNode]()

    init(_ root: TreeNode?) {
        self.root = root!
        var q = [self.root]
        var qi = 0
        while qi < q.count {
            let node = q[qi]
            qi += 1
            if let left = node.left { q.append(left) }
            else { parents.append(node); break }
            if let right = node.right { q.append(right) }
            else { parents.append(node); break }
        }
        while qi < q.count {
            parents.append(q[qi])
            qi += 1
        }
    }

    func insert(_ val: Int) -> Int {
        let parent = parents[0]
        let child = TreeNode(val)
        if parent.left == nil {
            parent.left = child
        } else {
            parent.right = child
            parents.removeFirst()
        }
        parents.append(child)
        return parent.val
    }

    func get_root() -> TreeNode? {
        return root
    }

    func getRoot() -> TreeNode? {
        return root
    }
}
