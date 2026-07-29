// LeetCode 1104 - Path In Zigzag Labelled Binary Tree
// https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

#include <stdlib.h>

int* pathInZigZagTree(int label, int* returnSize) {
    int tmp[32];
    int len = 0;
    tmp[len++] = label;
    while (label > 1) {
        int level = 0;
        int x = label;
        while (x) { level++; x >>= 1; }
        level -= 1;
        label >>= 1;
        label = (1 << level) - 1 - label + (1 << (level - 1));
        tmp[len++] = label;
    }
    int* ans = (int*)malloc((size_t)len * sizeof(int));
    for (int i = 0; i < len; i++) ans[i] = tmp[len - 1 - i];
    *returnSize = len;
    return ans;
}
