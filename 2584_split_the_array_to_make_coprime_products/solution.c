// LeetCode 2584 - Split the Array to Make Coprime Products
// https://leetcode.com/problems/split-the-array-to-make-coprime-products/

#include <stdlib.h>
#include <string.h>

int findValidSplit(int* nums, int numsSize) {
    int n = numsSize;
    // map prime -> last index; use arrays keyed by prime value up to 1e6
    int* last = (int*)malloc(1000001 * sizeof(int));
    memset(last, -1, 1000001 * sizeof(int));
    for (int i = 0; i < n; i++) {
        int x = nums[i];
        for (int p = 2; (long long)p * p <= x; p++) {
            if (x % p == 0) {
                last[p] = i;
                while (x % p == 0) x /= p;
            }
        }
        if (x > 1) last[x] = i;
    }
    int far = 0;
    for (int i = 0; i < n - 1; i++) {
        int x = nums[i];
        for (int p = 2; (long long)p * p <= x; p++) {
            if (x % p == 0) {
                if (last[p] > far) far = last[p];
                while (x % p == 0) x /= p;
            }
        }
        if (x > 1 && last[x] > far) far = last[x];
        if (far == i) { free(last); return i; }
    }
    free(last);
    return -1;
}
