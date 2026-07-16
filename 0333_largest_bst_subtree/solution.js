// LeetCode 0333 - Largest BST Subtree
function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

var largestBSTSubtree = function(root) {
    let best = 0;

    const dfs = (node) => {
        if (!node) return [true, Number.MAX_SAFE_INTEGER, Number.MIN_SAFE_INTEGER, 0];

        const [leftOk, leftMin, leftMax, leftSize] = dfs(node.left);
        const [rightOk, rightMin, rightMax, rightSize] = dfs(node.right);

        if (leftOk && rightOk && leftMax < node.val && node.val < rightMin) {
            const size = leftSize + rightSize + 1;
            best = Math.max(best, size);
            return [true, Math.min(leftMin, node.val), Math.max(rightMax, node.val), size];
        }

        return [false, 0, 0, 0];
    };

    dfs(root);
    return best;
};
