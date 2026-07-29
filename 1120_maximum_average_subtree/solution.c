// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

typedef struct { int sum; int count; } Pair;

static double bestAvg;

static Pair dfs(struct TreeNode* node) {
    if (!node) return (Pair){0, 0};
    Pair L = dfs(node->left);
    Pair R = dfs(node->right);
    int sum = L.sum + R.sum + node->val;
    int count = L.count + R.count + 1;
    double avg = (double)sum / (double)count;
    if (avg > bestAvg) bestAvg = avg;
    return (Pair){sum, count};
}

double maximumAverageSubtree(struct TreeNode* root) {
    bestAvg = 0.0;
    dfs(root);
    return bestAvg;
}
