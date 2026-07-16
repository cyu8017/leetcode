// LeetCode 0536 - Construct Binary Tree from String
// https://leetcode.com/problems/construct-binary-tree-from-string/

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
    func str2tree(_ s: String) -> TreeNode? {
        if s.isEmpty {
            return nil
        }

        let chars = Array(s)
        var index = 0

        func parse() -> TreeNode? {
            if index >= chars.count {
                return nil
            }

            var sign = 1
            if chars[index] == "-" {
                sign = -1
                index += 1
            }

            var value = 0
            while index < chars.count, chars[index] >= "0", chars[index] <= "9" {
                value = value * 10 + Int(String(chars[index]))!
                index += 1
            }

            let node = TreeNode(sign * value)

            if index < chars.count, chars[index] == "(" {
                index += 1
                node.left = parse()
                index += 1
            }

            if index < chars.count, chars[index] == "(" {
                index += 1
                node.right = parse()
                index += 1
            }

            return node
        }

        return parse()
    }
}
