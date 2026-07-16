// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export class BSTIterator {
    private readonly stack: TreeNode[] = [];

    constructor(root: TreeNode | null) {
        this.pushLeft(root);
    }

    private pushLeft(node: TreeNode | null): void {
        while (node) {
            this.stack.push(node);
            node = node.left;
        }
    }

    next(): number {
        const node = this.stack.pop()!;
        this.pushLeft(node.right);
        return node.val;
    }

    hasNext(): boolean {
        return this.stack.length > 0;
    }
}