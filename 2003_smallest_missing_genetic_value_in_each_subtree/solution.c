// LeetCode 2003 - Smallest Missing Genetic Value in Each Subtree
// https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static void collect2003(int u, int** children, int* childCnt, int* nums, bool* seen) {
    if (seen[nums[u]]) return;
    seen[nums[u]] = true;
    for (int i = 0; i < childCnt[u]; i++) collect2003(children[u][i], children, childCnt, nums, seen);
}

int* smallestMissingValueSubtree(int* parents, int parentsSize, int* nums, int numsSize, int* returnSize) {
    (void)numsSize;
    int n = parentsSize;
    *returnSize = n;
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) ans[i] = 1;

    int* childCnt = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 1; i < n; i++) childCnt[parents[i]]++;
    int** children = (int**)malloc((size_t)n * sizeof(int*));
    int* childPos = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) children[i] = (int*)malloc((size_t)(childCnt[i] ? childCnt[i] : 1) * sizeof(int));
    for (int i = 1; i < n; i++) {
        int p = parents[i];
        children[p][childPos[p]++] = i;
    }

    int one = -1;
    for (int i = 0; i < n; i++) if (nums[i] == 1) { one = i; break; }
    if (one < 0) {
        for (int i = 0; i < n; i++) free(children[i]);
        free(children); free(childCnt); free(childPos);
        return ans;
    }

    int maxNum = 0;
    for (int i = 0; i < n; i++) if (nums[i] > maxNum) maxNum = nums[i];
    bool* seen = (bool*)calloc((size_t)(maxNum + n + 5), sizeof(bool));
    int miss = 1, node = one, prev = -1;
    while (node != -1) {
        for (int i = 0; i < childCnt[node]; i++) {
            int v = children[node][i];
            if (v != prev) collect2003(v, children, childCnt, nums, seen);
        }
        seen[nums[node]] = true;
        while (seen[miss]) miss++;
        ans[node] = miss;
        prev = node;
        node = parents[node];
    }

    free(seen);
    for (int i = 0; i < n; i++) free(children[i]);
    free(children); free(childCnt); free(childPos);
    return ans;
}
