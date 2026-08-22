// LeetCode 1850 - Minimum Adjacent Swaps to Reach the Kth Smallest Number
// https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/

#include <stdlib.h>
#include <string.h>

static void reverseRange(char* arr, int l, int r) {
    while (l < r) {
        char t = arr[l];
        arr[l] = arr[r];
        arr[r] = t;
        l++;
        r--;
    }
}

static void nextPermutation(char* arr, int n) {
    int i = n - 2;
    while (i >= 0 && arr[i] >= arr[i + 1]) i--;
    if (i < 0) {
        reverseRange(arr, 0, n - 1);
        return;
    }
    int j = n - 1;
    while (arr[j] <= arr[i]) j--;
    char t = arr[i];
    arr[i] = arr[j];
    arr[j] = t;
    reverseRange(arr, i + 1, n - 1);
}

int getMinSwaps(char* num, int k) {
    int n = (int)strlen(num);
    char* target = (char*)malloc((size_t)n + 1);
    strcpy(target, num);
    for (int i = 0; i < k; i++) nextPermutation(target, n);

    char* source = (char*)malloc((size_t)n + 1);
    strcpy(source, num);
    int swaps = 0;
    for (int i = 0; i < n; i++) {
        if (source[i] == target[i]) continue;
        int j = i;
        while (source[j] != target[i]) j++;
        while (j > i) {
            char t = source[j];
            source[j] = source[j - 1];
            source[j - 1] = t;
            swaps++;
            j--;
        }
    }
    free(source);
    free(target);
    return swaps;
}
