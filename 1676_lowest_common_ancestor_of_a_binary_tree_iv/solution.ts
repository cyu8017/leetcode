// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

interface TreeNode1676 {
    val: number;
    left: TreeNode1676 | null;
    right: TreeNode1676 | null;
}

function lowestCommonAncestor(root: TreeNode1676 | null, nodes: (TreeNode1676 | number)[]): TreeNode1676 | null {
    const targets = new Set(nodes);
    const match = (node: TreeNode1676): boolean => {
        if (targets.has(node)) return true;
        return targets.has(node.val);
    };
    const dfs = (node: TreeNode1676 | null): TreeNode1676 | null => {
        if (!node) return null;
        const l = dfs(node.left);
        const r = dfs(node.right);
        if (match(node) || (l && r)) return node;
        return l || r;
    };
    return dfs(root);
}
