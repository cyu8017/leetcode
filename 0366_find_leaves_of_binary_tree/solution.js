// LeetCode 0366 - Find Leaves of Binary Tree
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

var findLeaves = function(root) {
    const layers = [];

    const dfs = (node) => {
        if (!node) return -1;
        const height = Math.max(dfs(node.left), dfs(node.right)) + 1;
        if (!layers[height]) layers[height] = [];
        layers[height].push(node.val);
        return height;
    };

    dfs(root);
    return layers;
};
