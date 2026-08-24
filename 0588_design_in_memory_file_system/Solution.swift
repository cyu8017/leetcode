// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/

class FileSystem {
    private class Node {
        var isFile = false
        var content = ""
        var children = [String: Node]()
    }

    private let root = Node()

    init() {}

    func ls(_ path: String) -> [String] {
        if path == "/" { return root.children.keys.sorted() }
        let parts = split(path)
        var node = root
        for part in parts { node = node.children[part]! }
        if node.isFile { return [parts.last!] }
        return node.children.keys.sorted()
    }

    func mkdir(_ path: String) {
        var node = root
        for part in split(path) {
            if node.children[part] == nil { node.children[part] = Node() }
            node = node.children[part]!
        }
    }

    func addContentToFile(_ filePath: String, _ content: String) {
        let parts = split(filePath)
        var node = root
        for i in 0..<(parts.count - 1) {
            if node.children[parts[i]] == nil { node.children[parts[i]] = Node() }
            node = node.children[parts[i]]!
        }
        let name = parts.last!
        if node.children[name] == nil { node.children[name] = Node() }
        let file = node.children[name]!
        file.isFile = true
        file.content += content
    }

    func readContentFromFile(_ filePath: String) -> String {
        var node = root
        for part in split(filePath) { node = node.children[part]! }
        return node.content
    }

    private func split(_ path: String) -> [String] {
        path.split(separator: "/").map(String.init).filter { !$0.isEmpty }
    }
}
