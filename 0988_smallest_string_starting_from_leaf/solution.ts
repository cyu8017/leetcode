// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

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

export function smallestFromLeaf(root: TreeNode | null): string {
    let best = "~";
    const dfs = (node, path) => {
        if (!node) return;
        path = String.fromCharCode(97 + node.val) + path;
        if (!node.left && !node.right) {
            if (path < best) best = path;
            return;
        }
        dfs(node.left, path);
        dfs(node.right, path);
    };
    dfs(root, "");
    return best;
}
