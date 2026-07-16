// LeetCode 0297 - Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

import java.util.ArrayDeque

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Codec {
    fun serialize(root: TreeNode?): String {
        if (root == null) {
            return ""
        }
        val values = mutableListOf<String>()
        val queue = ArrayDeque<TreeNode?>()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            if (node == null) {
                values.add("")
            } else {
                values.add(node.`val`.toString())
                queue.add(node.left)
                queue.add(node.right)
            }
        }
        while (values.isNotEmpty() && values.last().isEmpty()) {
            values.removeAt(values.lastIndex)
        }
        return values.joinToString(",")
    }

    fun deserialize(data: String): TreeNode? {
        if (data.isEmpty()) {
            return null
        }
        val values = data.split(",")
        val root = TreeNode(values[0].toInt())
        val queue = ArrayDeque<TreeNode>()
        queue.add(root)
        var index = 1
        while (queue.isNotEmpty() && index < values.size) {
            val node = queue.removeFirst()
            if (index < values.size && values[index].isNotEmpty()) {
                node.left = TreeNode(values[index].toInt())
                queue.add(node.left)
            }
            index++
            if (index < values.size && values[index].isNotEmpty()) {
                node.right = TreeNode(values[index].toInt())
                queue.add(node.right)
            }
            index++
        }
        return root
    }
}
