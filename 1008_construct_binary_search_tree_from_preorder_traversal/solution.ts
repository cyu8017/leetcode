// LeetCode 1008 - Construct Binary Search Tree from Preorder Traversal
// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function bstFromPreorder(preorder: number[]): TreeNode | null {
    let i = 0;
    const build = (bound: number): TreeNode | null => {
        if (i === preorder.length || preorder[i] > bound) return null;
        const root = new TreeNode(preorder[i++]);
        root.left = build(root.val);
        root.right = build(bound);
        return root;
    };
    return build(Infinity);
}
