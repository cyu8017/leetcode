// LeetCode 2096 - Step-By-Step Directions From a Binary Tree Node to Another
// https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static bool path2096(struct TreeNode* node, int target, char* p, int* plen) {
    if (!node) return false;
    if (node->val == target) return true;
    p[(*plen)++] = 'L';
    if (path2096(node->left, target, p, plen)) return true;
    p[(*plen) - 1] = 'R';
    if (path2096(node->right, target, p, plen)) return true;
    (*plen)--;
    return false;
}

char* getDirections(struct TreeNode* root, int startValue, int destValue) {
    char ps[100001], pd[100001];
    int ls = 0, ld = 0;
    path2096(root, startValue, ps, &ls);
    path2096(root, destValue, pd, &ld);
    int i = 0;
    while (i < ls && i < ld && ps[i] == pd[i]) i++;
    int up = ls - i;
    char* ans = (char*)malloc((size_t)up + (size_t)(ld - i) + 1);
    int k = 0;
    for (int j = 0; j < up; j++) ans[k++] = 'U';
    for (int j = i; j < ld; j++) ans[k++] = pd[j];
    ans[k] = '\0';
    return ans;
}
