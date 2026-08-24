// LeetCode 0449 - Serialize and Deserialize BST
// https://leetcode.com/problems/serialize-and-deserialize-bst/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Codec {
    fun serialize(root: TreeNode?): String {
        val parts = mutableListOf<String>()
        fun preorder(node: TreeNode?) {
            if (node == null) {
                parts.add("#")
                return
            }
            parts.add(node.`val`.toString())
            preorder(node.left)
            preorder(node.right)
        }
        preorder(root)
        return parts.joinToString(",")
    }

    fun deserialize(data: String): TreeNode? {
        if (data.isEmpty()) {
            return null
        }
        val values = data.split(",").iterator()
        fun build(): TreeNode? {
            val token = values.next()
            if (token == "#") {
                return null
            }
            return TreeNode(token.toInt()).apply {
                left = build()
                right = build()
            }
        }
        return build()
    }
}
