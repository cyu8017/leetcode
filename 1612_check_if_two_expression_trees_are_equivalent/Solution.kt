// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

class Node(var `val`: String = "", var left: Node? = null, var right: Node? = null)

class Solution {
    fun checkEquivalence(root1: Any?, root2: Any?): Boolean {
        val a = HashMap<String, Int>()
        val b = HashMap<String, Int>()
        count(parse(root1), a)
        count(parse(root2), b)
        return a == b
    }

    private fun parse(data: Any?): Node? {
        if (data == null) return null
        if (data is Node) return data
        if (data !is String) return null
        val inner = data.trim().removePrefix("[").removeSuffix("]")
        if (inner.isEmpty()) return null
        val vals = inner.split(",")
        val nodes = vals.map { if (it == "null") null else Node(it) }
        var k = 1
        for (node in nodes) {
            if (node != null) {
                if (k < nodes.size) node.left = nodes[k++]
                if (k < nodes.size) node.right = nodes[k++]
            }
        }
        return nodes.firstOrNull()
    }

    private fun count(node: Node?, out: HashMap<String, Int>) {
        if (node == null) return
        if (node.`val` == "+") {
            count(node.left, out)
            count(node.right, out)
        } else {
            out[node.`val`] = out.getOrDefault(node.`val`, 0) + 1
        }
    }
}
