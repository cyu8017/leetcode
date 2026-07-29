// LeetCode 1022 - Sum of Root To Leaf Binary Numbers
// https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
function sumRootToLeaf(root) {
    const dfs = (node, value) => {
        if (!node)
            return 0;
        value = value * 2 + node.val;
        if (!node.left && !node.right)
            return value;
        return dfs(node.left, value) + dfs(node.right, value);
    };
    return dfs(root, 0);
}
