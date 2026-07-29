// LeetCode 0606 - Construct String from Binary Tree
// https://leetcode.com/problems/construct-string-from-binary-tree/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

static void append(char** buf, int* len, int* cap, const char* text) {
    int need = (int)strlen(text);
    if (*len + need + 1 > *cap) {
        *cap = (*cap + need + 1) * 2;
        *buf = (char*)realloc(*buf, (size_t)*cap);
    }
    memcpy(*buf + *len, text, (size_t)need);
    *len += need;
    (*buf)[*len] = '\0';
}

static void build(struct TreeNode* root, char** buf, int* len, int* cap) {
    if (!root) {
        return;
    }
    char num[16];
    snprintf(num, sizeof(num), "%d", root->val);
    append(buf, len, cap, num);
    if (root->left || root->right) {
        append(buf, len, cap, "(");
        build(root->left, buf, len, cap);
        append(buf, len, cap, ")");
    }
    if (root->right) {
        append(buf, len, cap, "(");
        build(root->right, buf, len, cap);
        append(buf, len, cap, ")");
    }
}

char* tree2str(struct TreeNode* root) {
    int len = 0, cap = 64;
    char* buf = (char*)malloc((size_t)cap);
    buf[0] = '\0';
    build(root, &buf, &len, &cap);
    return buf;
}
