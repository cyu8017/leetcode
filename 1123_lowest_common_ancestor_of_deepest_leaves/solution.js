// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var lcaDeepestLeaves = function(root) {
    const dfs = (node) => {
        if (!node) return [null, 0];
        const [ln, ld] = dfs(node.left);
        const [rn, rd] = dfs(node.right);
        if (ld > rd) return [ln, ld + 1];
        if (rd > ld) return [rn, rd + 1];
        return [node, ld + 1];
    };
    return dfs(root)[0];
};
