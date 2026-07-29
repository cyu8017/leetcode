// LeetCode 0666 - Path Sum IV
// https://leetcode.com/problems/path-sum-iv/

#include <stdbool.h>

int pathSum(int* nums, int numsSize) {
    int tree[5][9];
    bool present[5][9];
    for (int d = 0; d < 5; d++) for (int p = 0; p < 9; p++) { tree[d][p] = 0; present[d][p] = false; }
    for (int i = 0; i < numsSize; i++) {
        int depth = nums[i] / 100;
        int pos = (nums[i] / 10) % 10;
        int val = nums[i] % 10;
        tree[depth][pos] = val;
        present[depth][pos] = true;
    }
    int total = 0;
    int stackD[64], stackP[64], stackPath[64], top = 0;
    stackD[top] = 1; stackP[top] = 1; stackPath[top] = 0; top++;
    while (top > 0) {
        top--;
        int depth = stackD[top], pos = stackP[top], path = stackPath[top];
        if (!present[depth][pos]) continue;
        path += tree[depth][pos];
        int leftP = pos * 2 - 1, rightP = pos * 2;
        bool hasLeft = depth + 1 < 5 && leftP < 9 && present[depth + 1][leftP];
        bool hasRight = depth + 1 < 5 && rightP < 9 && present[depth + 1][rightP];
        if (!hasLeft && !hasRight) total += path;
        else {
            if (hasLeft) { stackD[top]=depth+1; stackP[top]=leftP; stackPath[top]=path; top++; }
            if (hasRight) { stackD[top]=depth+1; stackP[top]=rightP; stackPath[top]=path; top++; }
        }
    }
    return total;
}
