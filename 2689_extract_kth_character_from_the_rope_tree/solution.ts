// LeetCode 2689 - Extract Kth Character From The Rope Tree
// https://leetcode.com/problems/extract-kth-character-from-the-rope-tree/

export function getKthCharacter(root: any, k: any): any {
    const dfs = (node, kk) => {
        if (!node.left && !node.right) return node.val;
        let leftLen = 0;
        if (node.left) leftLen = node.left.len > 0 ? node.left.len : 1;
        if (kk <= leftLen) return dfs(node.left, kk);
        return dfs(node.right, kk - leftLen);
    };
    return dfs(root, k);
}
