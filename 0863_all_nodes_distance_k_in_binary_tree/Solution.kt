// LeetCode 0863 - All Nodes Distance K in Binary Tree
// https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun distanceK(root: TreeNode?, target: TreeNode?, k: Int): MutableList<Int> {
        var graph = HashMap<TreeNode, MutableList<TreeNode>>()
        build(root, null, graph)
        var queue = ArrayDeque<TreeNode>()
        var seen = HashSet<TreeNode>()
        queue.offer(target)
        seen.add(target)
        var dist = 0
        while (!queue.isEmpty()) {
            if (dist == k) {
                var ans = ArrayList<Int>()
                for (node in queue) { ans.add(node.`val`) }
                return ans
            }
            var size = queue.size
            for (i in 0 until size) {
                var node = queue.poll()
                for (nei in graph.getOrDefault(node, Collections.emptyList())) {
                    if (seen.add(nei)) queue.offer(nei)
                }
            }
            dist++
        }
        return ArrayList()
    }

    private fun build(node: TreeNode?, parent: TreeNode?, graph: MutableMap<TreeNode, MutableList<TreeNode>>) {
        if (node == null) return
        if (parent != null) {
            graph.computeIfAbsent(node, x -> ArrayList()).add(parent)
            graph.computeIfAbsent(parent, x -> ArrayList()).add(node)
        }
        build(node.left, node, graph)
        build(node.right, node, graph)
    }
}
