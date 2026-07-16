// LeetCode 0099 - Recover Binary Search Tree
// https://leetcode.com/problems/recover-binary-search-tree/

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

/**
 Do not return anything, modify root in-place instead.
 */
export function recoverTree(root: TreeNode | null): void {
    let first: TreeNode | null = null;
    let second: TreeNode | null = null;
    let previous: TreeNode | null = null;
    const stack: TreeNode[] = [];
    let current = root;

    while (current || stack.length > 0) {
        while (current) {
            stack.push(current);
            current = current.left;
        }
        current = stack.pop()!;
        if (previous && previous.val > current.val) {
            if (first === null) {
                first = previous;
            }
            second = current;
        }
        previous = current;
        current = current.right;
    }

    if (first && second) {
        const temp = first.val;
        first.val = second.val;
        second.val = temp;
    }
}
