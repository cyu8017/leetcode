// LeetCode 0366 - Find Leaves of Binary Tree

// https://leetcode.com/problems/find-leaves-of-binary-tree/



class TreeNode(var `val`: Int) {

    var left: TreeNode? = null

    var right: TreeNode? = null

}



class Solution {

    fun findLeaves(root: TreeNode?): List<List<Int>> {

        val layers = mutableListOf<MutableList<Int>>()

        dfs(root, layers)

        return layers

    }



    private fun dfs(node: TreeNode?, layers: MutableList<MutableList<Int>>): Int {

        if (node == null) {

            return -1

        }



        val height = maxOf(dfs(node.left, layers), dfs(node.right, layers)) + 1

        while (layers.size <= height) {

            layers.add(mutableListOf())

        }

        layers[height].add(node.`val`)

        return height

    }

}
