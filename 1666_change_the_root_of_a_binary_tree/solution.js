// LeetCode 1666 - Change the Root of a Binary Tree
// https://leetcode.com/problems/change-the-root-of-a-binary-tree/

/**
 * @param {object} root
 * @param {object} leaf
 * @return {object}
 */
var flipBinaryTree = function(root, leaf) {
    let node = leaf;
    while (node !== root) {
        const parent = node.parent;
        if (parent.left === node) parent.left = null;
        else parent.right = null;
        const originalLeft = node.left;
        node.left = parent;
        if (originalLeft !== null) node.right = originalLeft;
        node = parent;
    }
    const fixParent = (cur, parent) => {
        if (!cur) return;
        cur.parent = parent;
        fixParent(cur.left, cur);
        fixParent(cur.right, cur);
    };
    fixParent(leaf, null);
    return leaf;
};
