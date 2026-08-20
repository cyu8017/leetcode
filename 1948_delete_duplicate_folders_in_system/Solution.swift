// LeetCode 1948 - Delete Duplicate Folders in System
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

class Solution {
    class Node {
        var children: [String: Node] = [:]
        var serial: String = ""
    }

    func deleteDuplicateFolder(_ paths: [[String]]) -> [[String]] {
        let root = Node()
        for path in paths {
            var node = root
            for folder in path {
                if node.children[folder] == nil {
                    node.children[folder] = Node()
                }
                node = node.children[folder]!
            }
        }
        var dup: [String: Bool] = [:]
        func serialize(_ node: Node) -> String {
            if node.children.isEmpty { return "" }
            var parts: [String] = []
            for name in node.children.keys.sorted() {
                parts.append(name + "(" + serialize(node.children[name]!) + ")")
            }
            let serial = parts.joined()
            if !serial.isEmpty {
                if dup[serial] != nil {
                    dup[serial] = true
                } else {
                    dup[serial] = false
                }
                node.serial = serial
            }
            return serial
        }
        _ = serialize(root)
        var ans: [[String]] = []
        func collect(_ node: Node, _ path: inout [String]) {
            for (name, child) in node.children {
                let serial = child.serial
                if !serial.isEmpty, dup[serial] == true { continue }
                path.append(name)
                ans.append(path)
                collect(child, &path)
                path.removeLast()
            }
        }
        var path: [String] = []
        collect(root, &path)
        return ans
    }
}
