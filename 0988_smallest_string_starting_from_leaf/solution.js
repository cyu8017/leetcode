// LeetCode 0988 - Smallest String Starting From Leaf
// https://leetcode.com/problems/smallest-string-starting-from-leaf/

/**
 * @param {TreeNode} root
 * @return {string}
 */
var smallestFromLeaf = function(root) {
    let best = "~";
    const dfs = (node, path) => {
        if (!node) return;
        path = String.fromCharCode(97 + node.val) + path;
        if (!node.left && !node.right) {
            if (path < best) best = path;
            return;
        }
        dfs(node.left, path);
        dfs(node.right, path);
    };
    dfs(root, "");
    return best;
};
