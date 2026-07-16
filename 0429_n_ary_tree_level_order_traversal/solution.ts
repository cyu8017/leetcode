// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

export class Node {
    val: number | null;
    children: Node[];

    constructor(val: number | null = null, children: Node[] | null = null) {
        this.val = val;
        this.children = children ?? [];
    }
}

export class Solution {
    levelOrder(root: Node | null): number[][] {
        if (!root) return [];

        const result: number[][] = [];
        const queue: Node[] = [root];

        while (queue.length > 0) {
            const level: number[] = [];
            const size = queue.length;
            for (let i = 0; i < size; i += 1) {
                const node = queue.shift() as Node;
                level.push(node.val as number);
                queue.push(...node.children);
            }
            result.push(level);
        }

        return result;
    }
}
