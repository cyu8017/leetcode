// LeetCode 0919 - Complete Binary Tree Inserter
// https://leetcode.com/problems/complete-binary-tree-inserter/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class CBTInserter(root: TreeNode?) {
    private val root = root!!
    private val parents = ArrayDeque<TreeNode>()

    init {
        val q = ArrayDeque<TreeNode>()
        q.add(this.root)
        while (q.isNotEmpty()) {
            val node = q.removeFirst()
            if (node.left != null) {
                q.add(node.left!!)
            } else {
                parents.add(node)
                break
            }
            if (node.right != null) {
                q.add(node.right!!)
            } else {
                parents.add(node)
                break
            }
        }
        while (q.isNotEmpty()) parents.add(q.removeFirst())
    }

    fun insert(`val`: Int): Int {
        val parent = parents.first()
        val child = TreeNode(`val`)
        if (parent.left == null) {
            parent.left = child
        } else {
            parent.right = child
            parents.removeFirst()
        }
        parents.add(child)
        return parent.`val`
    }

    fun getRoot(): TreeNode = root
}
