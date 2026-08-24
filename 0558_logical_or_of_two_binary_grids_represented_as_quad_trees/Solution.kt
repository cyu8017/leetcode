// LeetCode 0558 - Logical OR of Two Binary Grids Represented as Quad-Trees
// https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/

class Node(
    var `val`: Boolean = false,
    var isLeaf: Boolean = false,
    var topLeft: Node? = null,
    var topRight: Node? = null,
    var bottomLeft: Node? = null,
    var bottomRight: Node? = null
)

class Solution {
    fun intersect(quadTree1: Node?, quadTree2: Node?): Node? {
        val a = quadTree1!!
        val b = quadTree2!!
        if (a.isLeaf) return if (a.`val`) a else b
        if (b.isLeaf) return if (b.`val`) b else a
        val topLeft = intersect(a.topLeft, b.topLeft)!!
        val topRight = intersect(a.topRight, b.topRight)!!
        val bottomLeft = intersect(a.bottomLeft, b.bottomLeft)!!
        val bottomRight = intersect(a.bottomRight, b.bottomRight)!!
        if (topLeft.isLeaf && topRight.isLeaf && bottomLeft.isLeaf && bottomRight.isLeaf
            && topLeft.`val` == topRight.`val` && topRight.`val` == bottomLeft.`val`
            && bottomLeft.`val` == bottomRight.`val`) {
            return Node(topLeft.`val`, true)
        }
        return Node(false, false, topLeft, topRight, bottomLeft, bottomRight)
    }
}
