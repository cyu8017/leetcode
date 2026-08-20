// LeetCode 1305 - All Elements in Two Binary Search Trees
// https://leetcode.com/problems/all-elements-in-two-binary-search-trees/

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
    func getAllElements(_ root1: TreeNode?, _ root2: TreeNode?) -> [Int] {
        func inorder(_ root: TreeNode?) -> [Int] {
            guard let root = root else { return [] }
            return inorder(root.left) + [root.val] + inorder(root.right)
        }
        let a = inorder(root1), b = inorder(root2)
        var answer = [Int](), i = 0, j = 0
        while i < a.count || j < b.count {
            if j == b.count || (i < a.count && a[i] <= b[j]) {
                answer.append(a[i]); i += 1
            } else {
                answer.append(b[j]); j += 1
            }
        }
        return answer
    }
}
