// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/

#include <stddef.h>

struct Node {
    int val;
    int numChildren;
    struct Node** children;
};

static int answer1522;

static int depth1522(struct Node* node) {
    int longest = 0, second = 0;
    for (int i = 0; i < node->numChildren; i++) {
        int value = depth1522(node->children[i]) + 1;
        if (value > longest) {
            second = longest;
            longest = value;
        } else if (value > second) {
            second = value;
        }
    }
    if (longest + second > answer1522) answer1522 = longest + second;
    return longest;
}

int diameter(struct Node* root) {
    answer1522 = 0;
    if (root) depth1522(root);
    return answer1522;
}
