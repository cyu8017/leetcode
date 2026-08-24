// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

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
export function isCompleteTree(root: TreeNode | null): boolean {
    const q = [root];
    let end = false;
    while (q.length) {
        const node = q.shift();
        if (node === null) end = true;
        else {
            if (end) return false;
            q.push(node.left);
            q.push(node.right);
        }
    }
    return true;
}
