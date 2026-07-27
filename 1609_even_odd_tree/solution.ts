// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

function isEvenOddTree(root: TreeNode | null): boolean {
    let q: TreeNode[] = root ? [root] : [];
    let level = 0;
    while (q.length) {
        let prev = level % 2 === 0 ? -Infinity : Infinity;
        const nxt: TreeNode[] = [];
        for (const node of q) {
            if (node.val % 2 === level % 2) return false;
            if (level % 2 === 0 && node.val <= prev) return false;
            if (level % 2 === 1 && node.val >= prev) return false;
            prev = node.val;
            if (node.left) nxt.push(node.left);
            if (node.right) nxt.push(node.right);
        }
        q = nxt;
        level++;
    }
    return true;
}
