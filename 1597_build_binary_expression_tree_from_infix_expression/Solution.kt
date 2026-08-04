// LeetCode 1597 - Build Binary Expression Tree From Infix Expression
// https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/

import java.util.ArrayDeque

class Node {
    var `val`: Char = ' '
    var left: Node? = null
    var right: Node? = null

    constructor(`val`: Char) {
        this.`val` = `val`
    }

    constructor(`val`: Char, left: Node?, right: Node?) {
        this.`val` = `val`
        this.left = left
        this.right = right
    }
}

class Solution {
    fun expTree(s: String): Node? {
        val nodes = ArrayDeque<Node>()
        val ops = ArrayDeque<Char>()
        val priority = mapOf('+' to 1, '-' to 1, '*' to 2, '/' to 2)
        for (ch in s) {
            when {
                ch in '0'..'9' -> nodes.push(Node(ch))
                ch == '(' -> ops.push(ch)
                ch == ')' -> {
                    while (ops.peek() != '(') apply(nodes, ops)
                    ops.pop()
                }
                else -> {
                    while (ops.isNotEmpty() && ops.peek() != '(' &&
                        priority[ops.peek()]!! >= priority[ch]!!
                    ) {
                        apply(nodes, ops)
                    }
                    ops.push(ch)
                }
            }
        }
        while (ops.isNotEmpty()) apply(nodes, ops)
        return nodes.peek()
    }

    private fun apply(nodes: ArrayDeque<Node>, ops: ArrayDeque<Char>) {
        val op = ops.pop()
        val right = nodes.pop()
        val left = nodes.pop()
        nodes.push(Node(op, left, right))
    }
}
