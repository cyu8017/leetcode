// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

function sumRootToLeaf(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null, value: number): number => {
        if (!node) return 0;
        value = value * 2 + node.val;
        if (!node.left && !node.right) return value;
        return dfs(node.left, value) + dfs(node.right, value);
    };
    return dfs(root, 0);
}
