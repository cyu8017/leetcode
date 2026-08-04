// LeetCode 1902 - Depth Of Bst Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

class Solution {
    fun maxDepthBST(order: IntArray): Int {
        val nodes = mutableListOf<Pair<Int, Int>>()
        var ans = 0
        for (value in order) {
            var i = nodes.binarySearch(value to 0, compareBy { it.first })
            if (i < 0) i = -i - 1
            var depth = 1
            if (i > 0) depth = maxOf(depth, nodes[i - 1].second + 1)
            if (i < nodes.size) depth = maxOf(depth, nodes[i].second + 1)
            nodes.add(i, value to depth)
            ans = maxOf(ans, depth)
        }
        return ans
    }
}
