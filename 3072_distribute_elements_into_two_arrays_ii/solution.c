// LeetCode 3072 - Distribute Elements Into Two Arrays II
// https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

#include <stdlib.h>
#include <string.h>

typedef struct { int n; int* c; } BIT;
static BIT* bit_new(int n) { BIT* b=(BIT*)malloc(sizeof(BIT)); b->n=n; b->c=(int*)calloc((size_t)(n+1),sizeof(int)); return b; }
static void bit_upd(BIT* b, int x, int d) { for (; x <= b->n; x += x & -x) b->c[x] += d; }
static int bit_qry(BIT* b, int x) { int s=0; for (; x>0; x -= x & -x) s += b->c[x]; return s; }
static int cmp_int(const void* a, const void* b) { return (*(const int*)a) - (*(const int*)b); }
static int lower_bound(int* a, int n, int x) {
    int l=0,r=n;
    while (l<r) { int m=(l+r)/2; if (a[m]<x) l=m+1; else r=m; }
    return l;
}

int* resultArray(int* nums, int numsSize, int* returnSize) {
    int* st = (int*)malloc((size_t)numsSize * sizeof(int));
    memcpy(st, nums, (size_t)numsSize * sizeof(int));
    qsort(st, (size_t)numsSize, sizeof(int), cmp_int);
    int n = numsSize;
    BIT* tree1 = bit_new(n + 1);
    BIT* tree2 = bit_new(n + 1);
    bit_upd(tree1, lower_bound(st, n, nums[0]) + 1, 1);
    bit_upd(tree2, lower_bound(st, n, nums[1]) + 1, 1);
    int* arr1 = (int*)malloc((size_t)n * sizeof(int));
    int* arr2 = (int*)malloc((size_t)n * sizeof(int));
    int n1 = 0, n2 = 0;
    arr1[n1++] = nums[0];
    arr2[n2++] = nums[1];
    for (int k = 2; k < n; k++) {
        int x = nums[k];
        int i = lower_bound(st, n, x) + 1;
        int a = n1 - bit_qry(tree1, i);
        int b = n2 - bit_qry(tree2, i);
        if (a > b || (a == b && n1 <= n2)) { arr1[n1++] = x; bit_upd(tree1, i, 1); }
        else { arr2[n2++] = x; bit_upd(tree2, i, 1); }
    }
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n1; i++) ans[i] = arr1[i];
    for (int i = 0; i < n2; i++) ans[n1 + i] = arr2[i];
    free(st); free(arr1); free(arr2); free(tree1->c); free(tree1); free(tree2->c); free(tree2);
    *returnSize = n;
    return ans;
}
