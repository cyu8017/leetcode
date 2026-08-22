// LeetCode 2094 - Finding 3-Digit Even Numbers
// https://leetcode.com/problems/finding-3-digit-even-numbers/

#include <stdlib.h>

int* findEvenNumbers(int* digits, int digitsSize, int* returnSize) {
    int freq[10] = {0};
    for (int i = 0; i < digitsSize; i++) freq[digits[i]]++;
    int* ans = (int*)malloc(450 * sizeof(int));
    int n = 0;
    for (int x = 100; x <= 998; x += 2) {
        int a = x / 100, b = (x / 10) % 10, c = x % 10;
        freq[a]--; freq[b]--; freq[c]--;
        if (freq[a] >= 0 && freq[b] >= 0 && freq[c] >= 0) ans[n++] = x;
        freq[a]++; freq[b]++; freq[c]++;
    }
    *returnSize = n;
    return ans;
}
