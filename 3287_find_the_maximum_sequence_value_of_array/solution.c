// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

enum { MAXV = 128 };

int maxValue(int* nums, int numsSize, int k) {
    int n = numsSize;
    /* left[i][j][v] too big - allocate flat */
    bool* left = (bool*)calloc((size_t)(n + 1) * (k + 1) * MAXV, sizeof(bool));
    #define L(i,j,v) left[((size_t)(i)*(k+1)+(j))*MAXV+(v)]
    L(0,0,0) = true;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= k; j++) {
            for (int v = 0; v < MAXV; v++) {
                if (!L(i,j,v)) continue;
                L(i+1,j,v) = true;
                if (j < k) L(i+1,j+1,v|nums[i]) = true;
            }
        }
    }
    bool* right = (bool*)calloc((size_t)(n + 1) * (k + 1) * MAXV, sizeof(bool));
    #define R(i,j,v) right[((size_t)(i)*(k+1)+(j))*MAXV+(v)]
    R(n,0,0) = true;
    for (int i = n - 1; i >= 0; i--) {
        for (int j = 0; j <= k; j++) {
            for (int v = 0; v < MAXV; v++) {
                if (!R(i+1,j,v)) continue;
                R(i,j,v) = true;
                if (j < k) R(i,j+1,v|nums[i]) = true;
            }
        }
    }
    int ans = 0;
    for (int mid = k; mid + k <= n; mid++) {
        for (int a = 0; a < MAXV; a++) {
            if (!L(mid,k,a)) continue;
            for (int b = 0; b < MAXV; b++) {
                if (R(mid,k,b) && (a ^ b) > ans) ans = a ^ b;
            }
        }
    }
    free(left); free(right);
    return ans;
}
