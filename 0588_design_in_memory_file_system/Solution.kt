// LeetCode 0588 - Design In-Memory File System
// https://leetcode.com/problems/design-in-memory-file-system/


class FileSystem {
    private class Node {
        var isFile = false
        var content = ""
        val children = sortedMapOf<String, Node>()
    }

    private val root = Node()

    fun ls(path: String): List<String> {
        if (path == "/") return root.children.keys.toList()
        val parts = split(path)
        var node = root
        for (part in parts) node = node.children[part]!!
        if (node.isFile) return listOf(parts.last())
        return node.children.keys.toList()
    }

    fun mkdir(path: String) {
        var node = root
        for (part in split(path)) {
            node = node.children.getOrPut(part) { Node() }
        }
    }

    fun addContentToFile(filePath: String, content: String) {
        val parts = split(filePath)
        var node = root
        for (i in 0 until parts.size - 1) {
            node = node.children.getOrPut(parts[i]) { Node() }
        }
        val file = node.children.getOrPut(parts.last()) { Node() }
        file.isFile = true
        file.content += content
    }

    fun readContentFromFile(filePath: String): String {
        var node = root
        for (part in split(filePath)) node = node.children[part]!!
        return node.content
    }

    private fun split(path: String): List<String> =
        path.split('/').filter { it.isNotEmpty() }
}
