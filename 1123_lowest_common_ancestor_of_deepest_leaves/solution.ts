// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

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

function lcaDeepestLeaves(root: TreeNode | null): TreeNode {
    const dfs = (node) => {
        if (!node) return [null, 0];
        const [ln, ld] = dfs(node.left);
        const [rn, rd] = dfs(node.right);
        if (ld > rd) return [ln, ld + 1];
        if (rd > ld) return [rn, rd + 1];
        return [node, ld + 1];
    };
    return dfs(root)[0];
}
