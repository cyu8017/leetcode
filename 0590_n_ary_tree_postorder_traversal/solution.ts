// LeetCode 0590 - N-ary Tree Postorder Traversal
// https://leetcode.com/problems/n-ary-tree-postorder-traversal/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function postorder(root: Node | null | null): number[] {
    const result = [];
    const dfs = (node) => {
        if (node == null) return;
        if (node.children) for (const child of node.children) dfs(child);
        result.push(node.val);
    };
    dfs(root);
    return result;
}
