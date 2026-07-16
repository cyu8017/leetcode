// LeetCode 0199 - Binary Tree Right Side View
// https://leetcode.com/problems/binary-tree-right-side-view/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

export function rightSideView(root: TreeNode | null): number[] {
    if (!root) {
        return [];
    }

    const result: number[] = [];
    const queue: TreeNode[] = [root];
    let head = 0;
    while (head < queue.length) {
        const levelEnd = queue.length;
        while (head < levelEnd) {
            const node = queue[head++];
            if (head === levelEnd) {
                result.push(node.val);
            }
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
    }
    return result;
}