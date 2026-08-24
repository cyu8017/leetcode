// LeetCode 0559 - Maximum Depth of N-ary Tree
// https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function maxDepth(root: Node | null | null): number {
    if (root == null) return 0;
    if (!root.children || root.children.length === 0) return 1;
    let best = 0;
    for (const child of root.children) best = Math.max(best, maxDepth(child));
    return best + 1;
}
