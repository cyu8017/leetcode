// LeetCode 1628 - Design an Expression Tree With Evaluate Function
// https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/

abstract class Node {
    abstract fun evaluate(): Int
    companion object {
        fun leaf(`val`: String) = object : Node() {
            override fun evaluate() = `val`.toInt()
        }
        fun op(op: String, left: Node, right: Node) = object : Node() {
            override fun evaluate(): Int {
                val a = left.evaluate()
                val b = right.evaluate()
                return when (op) {
                    "+" -> a + b
                    "-" -> a - b
                    "*" -> a * b
                    else -> a / b
                }
            }
        }
    }
}

class TreeBuilder {
    fun expTree(postfix: Array<String>): Node {
        val stack = ArrayDeque<Node>()
        for (token in postfix) {
            if (token in setOf("+", "-", "*", "/")) {
                val right = stack.removeLast()
                val left = stack.removeLast()
                stack.addLast(Node.op(token, left, right))
            } else {
                stack.addLast(Node.leaf(token))
            }
        }
        return stack.last()
    }
}
