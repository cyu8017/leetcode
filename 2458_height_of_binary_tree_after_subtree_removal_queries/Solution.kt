// LeetCode 2458 - Height of Binary Tree After Subtree Removal Queries
// https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/

import java.util.ArrayList
import java.util.HashMap

class Solution {
    private var height: MutableMap<Int, Int> = HashMap()
    private var level: MutableMap<Int, Int> = HashMap()
    private var levelMax: MutableMap<Int, MutableList<Int>> = HashMap()
    fun treeQueries(root: TreeNode, queries: IntArray): IntArray {
            dfs(root, 0)
            var ans: IntArray = IntArray(queries.size)
            var i: Int = 0
    while (i < queries.size) {
    
                var q: Int = queries[i]
                var d: Int = level.get(q)
                var h: Int = height.get(q)
                var top: MutableList<Int> = levelMax.get(d)
                if (top.get(0) == h) {
                    if (top.size > 1) ans[i] = d + top.get(1)
                    else ans[i] = d - 1
                } else {
                    ans[i] = d + top.get(0)
                }
    
    i = i + 1
    }
            return ans
    }
    private fun dfs(node: TreeNode, d: Int): Int {
            if (node == null) return -1
            level.put(node.val, d)
            var h: Int = 1 + maxOf(dfs(node.left, d + 1), dfs(node.right, d + 1))
            height.put(node.val, h)
            var arr: MutableList<Int> = levelMax.getOrPut(d) { ArrayList() }
            if (arr.isEmpty()) arr.add(h)
            else if (h >= arr.get(0)) {
                if (arr.size == 1) arr.add(arr.get(0))
                else arr.set(1, arr.get(0))
                arr.set(0, h)
            } else if (arr.size == 1 || h > arr.get(1)) {
                if (arr.size == 1) arr.add(h)
                else arr.set(1, h)
            }
            return h
    }
}

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}
