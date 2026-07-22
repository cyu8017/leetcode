// LeetCode 1612 - Check If Two Expression Trees are Equivalent
// https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/

#include <stdbool.h>

struct Node {
    char val;
    struct Node* left;
    struct Node* right;
};

static void countLetters(struct Node* node, int* cnt) {
    if (!node) return;
    if (node->val == '+') {
        countLetters(node->left, cnt);
        countLetters(node->right, cnt);
    } else {
        cnt[node->val - 'a']++;
    }
}

bool checkEquivalence(struct Node* root1, struct Node* root2) {
    int a[26] = {0}, b[26] = {0};
    countLetters(root1, a);
    countLetters(root2, b);
    for (int i = 0; i < 26; i++) if (a[i] != b[i]) return false;
    return true;
}
