// LeetCode 0337 - House Robber III
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

var rob = function(root) {
    const dfs = (node) => {
        if (!node) return [0, 0];
        const [leftWith, leftWithout] = dfs(node.left);
        const [rightWith, rightWithout] = dfs(node.right);
        const withRob = node.val + leftWithout + rightWithout;
        const withoutRob = Math.max(leftWith, leftWithout) + Math.max(rightWith, rightWithout);
        return [withRob, withoutRob];
    };

    const [withRob, withoutRob] = dfs(root);
    return Math.max(withRob, withoutRob);
};
