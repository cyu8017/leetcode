// LeetCode 0951 - Flip Equivalent Binary Trees
// https://leetcode.com/problems/flip-equivalent-binary-trees/

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

function TreeNode(val: any, left: any, right: any): any {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}
export function flipEquiv(root1: TreeNode | null, root2: TreeNode | null): boolean {
    if (!root1 && !root2) return true;
    if (!root1 || !root2 || root1.val !== root2.val) return false;
    return (flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right)) ||
           (flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left));
}
