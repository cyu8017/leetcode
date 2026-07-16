// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

class Node {
    var val: Int
    var children: [Node]
    init(_ val: Int, _ children: [Node] = []) {
        self.val = val
        self.children = children
    }
}

class Codec {
    func encode(_ root: Node?) -> String {
        guard let root else {
            return ""
        }

        var parts: [String] = []
        var queue: [Node] = [root]
        while !queue.isEmpty {
            let node = queue.removeFirst()
            parts.append(String(node.val))
            parts.append(String(node.children.count))
            for child in node.children {
                parts.append(String(child.val))
                queue.append(child)
            }
        }
        return parts.joined(separator: ",")
    }

    func decode(_ data: String) -> Node? {
        if data.isEmpty {
            return nil
        }

        let values = data.split(separator: ",", omittingEmptySubsequences: false).map(String.init)
        var index = 0

        let rootValue = Int(values[index])!
        let rootChildCount = Int(values[index + 1])!
        index += 2
        let root = Node(rootValue)
        for _ in 0..<rootChildCount {
            root.children.append(Node(Int(values[index])!))
            index += 1
        }

        var queue = root.children
        while !queue.isEmpty {
            let node = queue.removeFirst()
            let childCount = Int(values[index + 1])!
            index += 2
            for _ in 0..<childCount {
                let child = Node(Int(values[index])!)
                node.children.append(child)
                queue.append(child)
                index += 1
            }
        }

        return root
    }

    func serialize(_ root: Node?) -> String {
        return encode(root)
    }

    func deserialize(_ data: String) -> Node? {
        return decode(data)
    }
}
