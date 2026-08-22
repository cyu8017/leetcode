// LeetCode 2122 - Recover the Original Array
// https://leetcode.com/problems/recover-the-original-array/

#include <stdlib.h>
#include <stdbool.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int* recoverArray(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* a = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) a[i] = nums[i];
    qsort(a, (size_t)n, sizeof(int), cmpInt);
    bool* used = (bool*)malloc((size_t)n * sizeof(bool));
    int* ans = (int*)malloc((size_t)(n / 2) * sizeof(int));
    for (int i = 1; i < n; i++) {
        int diff = a[i] - a[0];
        if (diff == 0 || diff % 2 != 0) continue;
        int k = diff / 2;
        for (int j = 0; j < n; j++) used[j] = false;
        used[0] = used[i] = true;
        int alen = 0;
        ans[alen++] = (a[0] + a[i]) / 2;
        int l = 0, r = i;
        bool ok = true;
        while (alen < n / 2) {
            while (l < n && used[l]) l++;
            if (l == n) { ok = false; break; }
            int need = a[l] + 2 * k;
            while (r < n && (used[r] || a[r] < need)) r++;
            if (r == n || a[r] != need) { ok = false; break; }
            used[l] = used[r] = true;
            ans[alen++] = a[l] + k;
        }
        if (ok) {
            free(a); free(used);
            *returnSize = alen;
            return ans;
        }
    }
    free(a); free(used); free(ans);
    *returnSize = 0;
    return NULL;
}
