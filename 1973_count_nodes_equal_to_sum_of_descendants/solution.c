// LeetCode 1973 - Count Nodes Equal to Sum of Descendants
// https://leetcode.com/problems/count-nodes-equal-to-sum-of-descendants/

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

static long long dfs(struct TreeNode* node, int* ans) {
    if (!node) return 0;
    long long total = dfs(node->left, ans) + dfs(node->right, ans);
    if (total == node->val) (*ans)++;
    return total + node->val;
}

int equalToDescendants(struct TreeNode* root) {
    int ans = 0;
    dfs(root, &ans);
    return ans;
}
