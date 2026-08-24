// LeetCode 3831 - Median Of A Binary Search Tree Level
// https://leetcode.com/problems/median_of_a_binary_search_tree_level/

export function levelMedian(root: any, level: any): any {
    const nums = [];
    const dfs = (node, i) => {
        if (!node) return;
        dfs(node.left, i + 1);
        if (i === level) nums.push(node.val);
        dfs(node.right, i + 1);
    };
    dfs(root, 0);
    if (!nums.length) return -1;
    return nums[Math.floor(nums.length / 2)];
}
