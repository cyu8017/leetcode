// LeetCode 1766 - Tree of Coprimes
// https://leetcode.com/problems/tree-of-coprimes/

#include <stdlib.h>

static int gcdInt(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a;
}

typedef struct {
    int* adjHead;
    int* adjNext;
    int* adjTo;
    int* nums;
    int* ans;
    int* pathDepth[51];
    int* pathNode[51];
    int pathLen[51];
} Ctx;

static void dfs(Ctx* ctx, int node, int parent, int depth) {
    int bestDepth = -1;
    int bestNode = -1;
    int val = ctx->nums[node];
    for (int d = 1; d <= 50; d++) {
        if (gcdInt(val, d) == 1 && ctx->pathLen[d] > 0) {
            int top = ctx->pathLen[d] - 1;
            if (ctx->pathDepth[d][top] > bestDepth) {
                bestDepth = ctx->pathDepth[d][top];
                bestNode = ctx->pathNode[d][top];
            }
        }
    }
    ctx->ans[node] = bestNode;
    ctx->pathDepth[val][ctx->pathLen[val]] = depth;
    ctx->pathNode[val][ctx->pathLen[val]] = node;
    ctx->pathLen[val]++;
    for (int e = ctx->adjHead[node]; e != -1; e = ctx->adjNext[e]) {
        int nxt = ctx->adjTo[e];
        if (nxt != parent) {
            dfs(ctx, nxt, node, depth + 1);
        }
    }
    ctx->pathLen[val]--;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getCoprimes(int* nums, int numsSize, int** edges, int edgesSize, int* edgesColSize, int* returnSize) {
    int n = numsSize;
    Ctx ctx;
    ctx.nums = nums;
    ctx.adjHead = (int*)malloc(n * sizeof(int));
    ctx.adjNext = (int*)malloc((size_t)2 * edgesSize * sizeof(int));
    ctx.adjTo = (int*)malloc((size_t)2 * edgesSize * sizeof(int));
    for (int i = 0; i < n; i++) {
        ctx.adjHead[i] = -1;
    }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0];
        int b = edges[i][1];
        ctx.adjTo[2 * i] = b;
        ctx.adjNext[2 * i] = ctx.adjHead[a];
        ctx.adjHead[a] = 2 * i;
        ctx.adjTo[2 * i + 1] = a;
        ctx.adjNext[2 * i + 1] = ctx.adjHead[b];
        ctx.adjHead[b] = 2 * i + 1;
    }
    ctx.ans = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        ctx.ans[i] = -1;
    }
    for (int v = 1; v <= 50; v++) {
        ctx.pathDepth[v] = (int*)malloc(n * sizeof(int));
        ctx.pathNode[v] = (int*)malloc(n * sizeof(int));
        ctx.pathLen[v] = 0;
    }
    dfs(&ctx, 0, -1, 0);
    for (int v = 1; v <= 50; v++) {
        free(ctx.pathDepth[v]);
        free(ctx.pathNode[v]);
    }
    free(ctx.adjHead);
    free(ctx.adjNext);
    free(ctx.adjTo);
    *returnSize = n;
    return ctx.ans;
}
