// LeetCode 0094 - Binary Tree Inorder Traversal
// https://leetcode.com/problems/binary-tree-inorder-traversal/

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

export function inorderTraversal(root: TreeNode | null): number[] {
    const result: number[] = [];
    const stack: TreeNode[] = [];
    let current: TreeNode | null = root;
    while (current || stack.length) {
        while (current) {
            stack.push(current);
            current = current.left;
        }
        current = stack.pop()!;
        result.push(current.val);
        current = current.right;
    }
    return result;
}
