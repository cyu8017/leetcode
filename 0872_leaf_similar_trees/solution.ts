// LeetCode 0872 - Leaf-Similar Trees
// https://leetcode.com/problems/leaf-similar-trees/

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

export function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
    const leaves = (node) => {
        const result = [];
        const dfs = (cur) => {
            if (!cur) return;
            if (!cur.left && !cur.right) {
                result.push(cur.val);
                return;
            }
            dfs(cur.left);
            dfs(cur.right);
        };
        dfs(node);
        return result;
    };
    const a = leaves(root1), b = leaves(root2);
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) if (a[i] !== b[i]) return false;
    return true;
}
