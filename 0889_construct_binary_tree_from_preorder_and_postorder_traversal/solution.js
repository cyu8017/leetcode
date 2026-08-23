// LeetCode 0889 - Construct Binary Tree from Preorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {number[]} preorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */
var constructFromPrePost = function(preorder, postorder) {
    const postIndex = new Map();
    for (let i = 0; i < postorder.length; i++) postIndex.set(postorder[i], i);
    const build = (preLo, preHi, postLo, postHi) => {
        if (preLo > preHi) return null;
        const root = new TreeNode(preorder[preLo]);
        if (preLo === preHi) return root;
        const leftVal = preorder[preLo + 1];
        const leftPost = postIndex.get(leftVal);
        const leftSize = leftPost - postLo + 1;
        root.left = build(preLo + 1, preLo + leftSize, postLo, leftPost);
        root.right = build(preLo + leftSize + 1, preHi, leftPost + 1, postHi - 1);
        return root;
    };
    const n = preorder.length;
    return build(0, n - 1, 0, n - 1);
};
