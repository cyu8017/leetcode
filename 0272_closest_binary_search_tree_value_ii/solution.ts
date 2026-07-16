// LeetCode 0272 - Closest Binary Search Tree Value II
// https://leetcode.com/problems/closest-binary-search-tree-value-ii/

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

function closestKValues(root: TreeNode | null, target: number, k: number): number[] {
    const values: number[] = [];

    const inorder = (node: TreeNode | null): void => {
        if (!node) {
            return;
        }
        inorder(node.left);
        values.push(node.val);
        inorder(node.right);
    };

    inorder(root);

    let lo = 0;
    let hi = values.length;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (values[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid;
        }
    }

    let left = lo - 1;
    let right = lo;
    const result: number[] = [];
    while (result.length < k) {
        if (
            right >= values.length ||
            (left >= 0 && Math.abs(values[left] - target) <= Math.abs(values[right] - target))
        ) {
            result.push(values[left]);
            left -= 1;
        } else {
            result.push(values[right]);
            right += 1;
        }
    }
    return result;
}
