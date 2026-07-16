// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

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

class Codec {
    func serialize(_ root: TreeNode?) -> String {
        var parts: [String] = []

        func preorder(_ node: TreeNode?) {
            guard let node else {
                parts.append("#")
                return
            }
            parts.append(String(node.val))
            preorder(node.left)
            preorder(node.right)
        }

        preorder(root)
        return parts.joined(separator: ",")
    }

    func deserialize(_ data: String) -> TreeNode? {
        if data.isEmpty {
            return nil
        }
        var values = data.split(separator: ",", omittingEmptySubsequences: false).map(String.init)
        var index = 0

        func build() -> TreeNode? {
            guard index < values.count else {
                return nil
            }
            let token = values[index]
            index += 1
            if token == "#" {
                return nil
            }
            let node = TreeNode(Int(token)!)
            node.left = build()
            node.right = build()
            return node
        }

        return build()
    }
}
