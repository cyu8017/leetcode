// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

interface TreeNode1660 {
    val: number;
    left: TreeNode1660 | null;
    right: TreeNode1660 | null;
}

function correctBinaryTree(root: TreeNode1660 | null): TreeNode1660 | null {
    const seen = new Set<TreeNode1660>();
    const dfs = (node: TreeNode1660 | null): TreeNode1660 | null => {
        if (!node) return null;
        if (node.right && seen.has(node.right)) return null;
        seen.add(node);
        node.right = dfs(node.right);
        node.left = dfs(node.left);
        return node;
    };
    return dfs(root);
}
