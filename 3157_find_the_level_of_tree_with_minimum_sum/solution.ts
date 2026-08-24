// LeetCode 3157 - Find the Level of Tree with Minimum Sum
// https://leetcode.com/problems/find-the-level-of-tree-with-minimum-sum/

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

export function minimumLevel(root: TreeNode | null): number {
    const q = [root];
    let s = Number.MAX_SAFE_INTEGER;
    let ans = 0;
    for (let level = 1; q.length; level++) {
        let t = 0;
        let m = q.length;
        while (m-- > 0) {
            const node = q.shift();
            t += node.val;
            if (node.left !== null) q.push(node.left);
            if (node.right !== null) q.push(node.right);
        }
        if (s > t) {
            s = t;
            ans = level;
        }
    }
    return ans;
}
