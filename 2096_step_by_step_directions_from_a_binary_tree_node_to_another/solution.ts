// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

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

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function getDirections(root: TreeNode | null, startValue: number, destValue: number): string {
    const path = (node, target, p) => {
        if (node === null) return false;
        if (node.val === target) return true;
        p.push('L');
        if (path(node.left, target, p)) return true;
        p[p.length - 1] = 'R';
        if (path(node.right, target, p)) return true;
        p.pop();
        return false;
    };
    const ps = [], pd = [];
    path(root, startValue, ps);
    path(root, destValue, pd);
    let i = 0;
    while (i < ps.length && i < pd.length && ps[i] === pd[i]) i++;
    return 'U'.repeat(ps.length - i) + pd.slice(i).join('');
}
