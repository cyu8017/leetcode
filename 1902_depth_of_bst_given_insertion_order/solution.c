// LeetCode 1902 - Depth of BST Given Insertion Order
// https://leetcode.com/problems/depth-of-bst-given-insertion-order/

#include <stdlib.h>

int maxDepthBST(int* order, int orderSize) {
    int* vals = (int*)malloc((size_t)orderSize * sizeof(int));
    int* depths = (int*)malloc((size_t)orderSize * sizeof(int));
    int n = 0, ans = 0;
    for (int t = 0; t < orderSize; t++) {
        int value = order[t];
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (vals[mid] < value) lo = mid + 1;
            else hi = mid;
        }
        int depth = 1;
        if (lo > 0 && depths[lo - 1] + 1 > depth) depth = depths[lo - 1] + 1;
        if (lo < n && depths[lo] + 1 > depth) depth = depths[lo] + 1;
        for (int i = n; i > lo; i--) {
            vals[i] = vals[i - 1];
            depths[i] = depths[i - 1];
        }
        vals[lo] = value;
        depths[lo] = depth;
        n++;
        if (depth > ans) ans = depth;
    }
    free(vals);
    free(depths);
    return ans;
}
