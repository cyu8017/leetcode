// LeetCode 0109 - Convert Sorted List to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

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
    func sortedListToBST(_ head: ListNode?) -> TreeNode? {
        var values = [Int]()
        var current = head
        while let node = current {
            values.append(node.val)
            current = node.next
        }

        func build(_ left: Int, _ right: Int) -> TreeNode? {
            if left > right {
                return nil
            }
            let mid = (left + right + 1) / 2
            let root = TreeNode(values[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        }

        return build(0, values.count - 1)
    }
}
