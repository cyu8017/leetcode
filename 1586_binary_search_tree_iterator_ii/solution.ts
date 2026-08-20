// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/
// @ts-nocheck

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export class BSTIterator {
    values: number[];
    index: number;

    constructor(root: TreeNode | null) {
        this.values = [];
        const stack = [];
        while (stack.length || root) {
            while (root) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            this.values.push(root.val);
            root = root.right;
        }
        this.index = -1;
    }

    hasNext(): boolean {
        return this.index + 1 < this.values.length;
    }

    next(): number {
        this.index++;
        return this.values[this.index];
    }

    hasPrev(): boolean {
        return this.index > 0;
    }

    prev(): number {
        this.index--;
        return this.values[this.index];
    }
}
