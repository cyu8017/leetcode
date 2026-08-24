// LeetCode 2476 - Closest Nodes Queries in a Binary Search Tree
// https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/

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

export function closestNodes(root: TreeNode | null, queries: number[]): number[][] {
    const vals = [];
    const inorder = (node) => {
        if (!node) return;
        inorder(node.left);
        vals.push(node.val);
        inorder(node.right);
    };
    inorder(root);
    const lowerBound = (q) => {
        let lo = 0, hi = vals.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (vals[mid] < q) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    const ans = [];
    for (const q of queries) {
        const j = lowerBound(q);
        const mx = j < vals.length ? vals[j] : -1;
        let mn = -1;
        if (j < vals.length && vals[j] === q) mn = q;
        else if (j > 0) mn = vals[j - 1];
        ans.push([mn, mx]);
    }
    return ans;
}
