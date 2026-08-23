// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var minCameraCover = function(root) {
    let cameras = 0;
    // 0 = needs camera, 1 = covered, 2 = has camera
    const dfs = (node) => {
        if (!node) return 1;
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (left === 0 || right === 0) {
            cameras++;
            return 2;
        }
        if (left === 2 || right === 2) return 1;
        return 0;
    };
    const rootState = dfs(root);
    return cameras + (rootState === 0 ? 1 : 0);
};
