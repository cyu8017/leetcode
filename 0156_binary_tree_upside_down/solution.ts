// LeetCode 0156 - Binary Tree Upside Down
// https://leetcode.com/problems/binary-tree-upside-down/

export interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export function upsideDownBinaryTree(root: TreeNode | null): TreeNode | null {
    let previous: TreeNode | null = null;
    let previousRight: TreeNode | null = null;
    let current: TreeNode | null = root;

    while (current !== null) {
        const next = current.left;
        current.left = previousRight;
        previousRight = current.right;
        current.right = previous;
        previous = current;
        current = next;
    }

    return previous;
}