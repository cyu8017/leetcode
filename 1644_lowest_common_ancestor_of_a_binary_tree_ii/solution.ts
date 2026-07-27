// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    let found = 0;
    const dfs = (node: TreeNode | null): TreeNode | null => {
        if (!node) return null;
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (node === p || node === q) {
            found++;
            return node;
        }
        return left && right ? node : left || right;
    };
    const ans = dfs(root);
    return found === 2 ? ans : null;
}
