// LeetCode 2265 - Count Nodes Equal to Average of Subtree
// https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static void dfs_avg(struct TreeNode* node, int* sum, int* cnt, int* ans) {
    if (!node) {
        *sum = 0;
        *cnt = 0;
        return;
    }
    int ls, lc, rs, rc;
    dfs_avg(node->left, &ls, &lc, ans);
    dfs_avg(node->right, &rs, &rc, ans);
    *sum = ls + rs + node->val;
    *cnt = lc + rc + 1;
    if (*sum / *cnt == node->val) (*ans)++;
}

int averageOfSubtree(struct TreeNode* root) {
    int ans = 0, sum = 0, cnt = 0;
    dfs_avg(root, &sum, &cnt, &ans);
    return ans;
}
