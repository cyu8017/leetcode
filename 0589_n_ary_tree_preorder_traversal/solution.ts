// LeetCode 0589 - N-ary Tree Preorder Traversal
// https://leetcode.com/problems/n-ary-tree-preorder-traversal/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function preorder(root: Node | null | null): number[] {
    const result = [];
    const dfs = (node) => {
        if (node == null) return;
        result.push(node.val);
        if (node.children) for (const child of node.children) dfs(child);
    };
    dfs(root);
    return result;
}
