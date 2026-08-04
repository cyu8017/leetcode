// LeetCode 1948
// https://leetcode.com/problems/delete-duplicate-folders-in-system/

class Solution {
    private class Node {
        val children = sortedMapOf<String, Node>()
        var serial = ""
        var deleted = false
    }

    fun deleteDuplicateFolder(paths: List<List<String>>): List<List<String>> {
        val root = Node()
        for (path in paths) {
            var node = root
            for (folder in path) node = node.children.getOrPut(folder) { Node() }
        }
        val serialCount = HashMap<String, Int>()
        fun serialize(node: Node): String {
            if (node.children.isEmpty()) return ""
            val parts = node.children.map { (name, child) -> "$name(${serialize(child)})" }
            val serial = parts.joinToString("")
            node.serial = serial
            if (serial.isNotEmpty()) serialCount[serial] = serialCount.getOrDefault(serial, 0) + 1
            return serial
        }
        serialize(root)
        fun mark(node: Node) {
            if (node.serial.isNotEmpty() && serialCount[node.serial]!! > 1) node.deleted = true
            for (child in node.children.values) mark(child)
        }
        mark(root)
        val ans = mutableListOf<List<String>>()
        fun collect(node: Node, path: MutableList<String>) {
            for ((name, child) in node.children) {
                if (child.deleted) continue
                path.add(name)
                ans.add(path.toList())
                collect(child, path)
                path.removeAt(path.lastIndex)
            }
        }
        collect(root, mutableListOf())
        return ans
    }
}
