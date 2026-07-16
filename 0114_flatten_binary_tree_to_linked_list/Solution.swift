class TreeNode {
    var val: Int
    var left: TreeNode?
    var right: TreeNode?
    init() { self.val = 0; self.left = nil; self.right = nil }
    init(_ val: Int) { self.val = val; self.left = nil; self.right = nil }
    init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
        self.val = val; self.left = left; self.right = right
    }
}

class Solution {
    func flatten(_ root: TreeNode?) {
        guard let root = root else { return }
        flatten(root.left)
        flatten(root.right)
        guard let left = root.left else { return }
        var tail = left
        while let next = tail.right { tail = next }
        tail.right = root.right
        root.right = left
        root.left = nil
    }
}