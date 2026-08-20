// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

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

class BSTIterator {
    private var values = [Int]()
    private var index = -1

    init(_ root: TreeNode?) {
        var stack = [TreeNode]()
        var node = root
        while !stack.isEmpty || node != nil {
            while let cur = node {
                stack.append(cur)
                node = cur.left
            }
            let cur = stack.removeLast()
            values.append(cur.val)
            node = cur.right
        }
    }

    func hasNext() -> Bool { index + 1 < values.count }

    func next() -> Int {
        index += 1
        return values[index]
    }

    func hasPrev() -> Bool { index > 0 }

    func prev() -> Int {
        index -= 1
        return values[index]
    }
}
