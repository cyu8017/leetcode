// LeetCode 2313 - Minimum Flips in Binary Tree to Get Result
// https://leetcode.com/problems/minimum-flips-in-binary-tree-to-get-result/

/**
 * @param {TreeNode} root
 * @param {boolean} result
 * @return {number}
 */
var minimumFlips = function(root, result) {
    const dfs = (node) => {
        if (node.left === null && node.right === null) {
            return node.val === 0 ? [0, 1] : [1, 0];
        }
        if (node.val === 5) {
            const x = dfs(node.left);
            return [x[1], x[0]];
        }
        const L = dfs(node.left), R = dfs(node.right);
        const lf = L[0], lt = L[1], rf = R[0], rt = R[1];
        if (node.val === 2) {
            return [lf + rf, Math.min(lt + rt, Math.min(lt + rf, lf + rt))];
        }
        if (node.val === 3) {
            return [Math.min(lf + rf, Math.min(lf + rt, lt + rf)), lt + rt];
        }
        if (node.val === 4) {
            return [Math.min(lf + rf, lt + rt), Math.min(lf + rt, lt + rf)];
        }
        return [0, 0];
    };
    const res = dfs(root);
    return result ? res[1] : res[0];
};
