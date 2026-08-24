// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export function tree2str(root: TreeNode | null): string {
    if (root == null) return "";
    let result = String(root.val);
    if (root.left != null || root.right != null) result += "(" + tree2str(root.left) + ")";
    if (root.right != null) result += "(" + tree2str(root.right) + ")";
    return result;
}
