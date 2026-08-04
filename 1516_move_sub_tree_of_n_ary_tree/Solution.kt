// LeetCode 1516 - Move Sub-Tree of N-Ary Tree
// https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

import java.util.IdentityHashMap

class Node(var `val`: Int) {
    var children: MutableList<Node> = mutableListOf()
}

class Solution {
    fun moveSubTree(root: Node?, p: Node, q: Node): Node? {
        var result = root
        val parent = IdentityHashMap<Node, Node>()
        build(result!!, parent)
        if (parent[p] === q) return result

        val pParent = parent[p]
        val qParent = parent[q]

        if (isAncestor(p, q, parent)) {
            qParent!!.children.remove(q)
            if (pParent == null) {
                result = q
            } else {
                val idx = pParent.children.indexOf(p)
                pParent.children[idx] = q
            }
            q.children.add(p)
        } else {
            if (pParent == null) {
                result = q
            } else {
                pParent.children.remove(p)
            }
            q.children.add(p)
        }
        return result
    }

    private fun build(node: Node, parent: IdentityHashMap<Node, Node>) {
        for (child in node.children) {
            parent[child] = node
            build(child, parent)
        }
    }

    private fun isAncestor(ancestor: Node, node: Node, parent: IdentityHashMap<Node, Node>): Boolean {
        var current: Node? = node
        while (current != null && parent.containsKey(current)) {
            current = parent[current]
            if (current === ancestor) return true
        }
        return false
    }
}
