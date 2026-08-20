// LeetCode 1932 - Merge BSTs to Create Single BST
// https://leetcode.com/problems/merge-bsts-to-create-single-bst/

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

function canMerge(trees: Array<TreeNode | null>): TreeNode | null {
    const valueToRoot = new Map<number, TreeNode>();
    const count = new Map<number, number>();
    for (const tree of trees) {
        if (!tree) continue;
        valueToRoot.set(tree.val, tree);
        count.set(tree.val, (count.get(tree.val) || 0) + 1);
        if (tree.left) count.set(tree.left.val, (count.get(tree.left.val) || 0) + 1);
        if (tree.right) count.set(tree.right.val, (count.get(tree.right.val) || 0) + 1);
    }
    const roots = trees.filter((t): t is TreeNode => !!t && count.get(t.val) === 1);
    if (roots.length !== 1) return null;
    const root = roots[0];
    const merge = (node: TreeNode | null): boolean => {
        if (!node) return true;
        if (node.left && valueToRoot.has(node.left.val)) {
            node.left = valueToRoot.get(node.left.val)!;
            valueToRoot.delete(node.left.val);
        }
        if (node.right && valueToRoot.has(node.right.val)) {
            node.right = valueToRoot.get(node.right.val)!;
            valueToRoot.delete(node.right.val);
        }
        return merge(node.left) && merge(node.right);
    };
    valueToRoot.delete(root.val);
    if (!merge(root) || valueToRoot.size) return null;
    const isValidBst = (node: TreeNode | null, lo: number, hi: number): boolean => {
        if (!node) return true;
        if (!(lo < node.val && node.val < hi)) return false;
        return isValidBst(node.left, lo, node.val) && isValidBst(node.right, node.val, hi);
    };
    return isValidBst(root, -Infinity, Infinity) ? root : null;
}
