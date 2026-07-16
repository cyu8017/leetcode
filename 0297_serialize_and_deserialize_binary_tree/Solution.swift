// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

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
        guard let root else {
            return ""
        }
        var values: [String] = []
        var queue: [TreeNode?] = [root]
        while !queue.isEmpty {
            let node = queue.removeFirst()
            if let node {
                values.append(String(node.val))
                queue.append(node.left)
                queue.append(node.right)
            } else {
                values.append("")
            }
        }
        while let last = values.last, last.isEmpty {
            values.removeLast()
        }
        return values.joined(separator: ",")
    }

    func deserialize(_ data: String) -> TreeNode? {
        if data.isEmpty {
            return nil
        }
        let values = data.split(separator: ",", omittingEmptySubsequences: false).map(String.init)
        let root = TreeNode(Int(values[0])!)
        var queue: [TreeNode] = [root]
        var index = 1
        while !queue.isEmpty && index < values.count {
            let node = queue.removeFirst()
            if index < values.count && !values[index].isEmpty {
                node.left = TreeNode(Int(values[index])!)
                queue.append(node.left!)
            }
            index += 1
            if index < values.count && !values[index].isEmpty {
                node.right = TreeNode(Int(values[index])!)
                queue.append(node.right!)
            }
            index += 1
        }
        return root
    }
}
