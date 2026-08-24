// LeetCode 0314 - Binary Tree Vertical Order Traversal

// https://leetcode.com/problems/binary-tree-vertical-order-traversal/



class TreeNode(var `val`: Int) {

    var left: TreeNode? = null

    var right: TreeNode? = null

}



class Solution {

    fun verticalOrder(root: TreeNode?): List<List<Int>> {

        if (root == null) {

            return emptyList()

        }



        val columns = mutableMapOf<Int, MutableList<Int>>()

        val nodes = ArrayDeque<TreeNode>()

        val columnIndexes = ArrayDeque<Int>()

        nodes.add(root)

        columnIndexes.add(0)

        var minCol = 0

        var maxCol = 0



        while (nodes.isNotEmpty()) {

            val node = nodes.removeFirst()

            val column = columnIndexes.removeFirst()

            minCol = minOf(minCol, column)

            maxCol = maxOf(maxCol, column)

            columns.getOrPut(column) { mutableListOf() }.add(node.`val`)

            node.left?.let {

                nodes.add(it)

                columnIndexes.add(column - 1)

            }

            node.right?.let {

                nodes.add(it)

                columnIndexes.add(column + 1)

            }

        }



        return (minCol..maxCol).map { columns[it]!! }

    }

}

