// LeetCode 3378 - Count Connected Components in LCM Graph
// https://leetcode.com/problems/count-connected-components-in-lcm-graph/

#include <stdlib.h>

static int gcd3378(int a, int b) { while (b) { int t = a % b; a = b; b = t; } return a; }
static int findp(int* p, int x) { return p[x] == x ? x : (p[x] = findp(p, p[x])); }
static void unite(int* p, int a, int b) { a = findp(p, a); b = findp(p, b); if (a != b) p[a] = b; }

int countComponents(int* nums, int numsSize, int threshold) {
    int n = numsSize;
    int* parent = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = i;
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) {
        int a = nums[i], b = nums[j], g = gcd3378(a, b);
        if ((long long)a / g * b <= threshold) unite(parent, i, j);
    }
    int* seen = (int*)calloc(n, sizeof(int));
    int comp = 0;
    for (int i = 0; i < n; i++) {
        int r = findp(parent, i);
        if (!seen[r]) { seen[r] = 1; comp++; }
    }
    free(parent); free(seen);
    return comp;
}
