// LeetCode 0428 - Serialize and Deserialize N-ary Tree
// https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

class Node(var `val`: Int? = null, val children: MutableList<Node> = mutableListOf())

class Codec {
    fun encode(root: Node?): String {
        if (root == null) {
            return ""
        }

        val parts = mutableListOf<String>()
        val queue = ArrayDeque<Node>()
        queue.add(root)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            parts.add(node.`val`.toString())
            parts.add(node.children.size.toString())
            for (child in node.children) {
                parts.add(child.`val`.toString())
                queue.add(child)
            }
        }
        return parts.joinToString(",")
    }

    fun decode(data: String): Node? {
        if (data.isEmpty()) {
            return null
        }

        val values = data.split(",")
        var index = 0

        fun readRoot(): Node {
            val value = values[index].toInt()
            val childCount = values[index + 1].toInt()
            index += 2
            val node = Node(value, mutableListOf())
            repeat(childCount) {
                node.children.add(Node(values[index].toInt(), mutableListOf()))
                index++
            }
            return node
        }

        val root = readRoot()
        val queue = ArrayDeque(root.children)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            val value = values[index].toInt()
            val childCount = values[index + 1].toInt()
            index += 2
            require(value == node.`val`) { "expected node value ${node.`val`}, found $value" }
            repeat(childCount) {
                val child = Node(values[index].toInt(), mutableListOf())
                node.children.add(child)
                queue.add(child)
                index++
            }
        }
        return root
    }
}
