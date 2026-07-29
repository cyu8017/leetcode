// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

#include <stdbool.h>
#include <string.h>

static void sig(int n, char* out) {
    int freq[10] = {0};
    if (n == 0) freq[0]++;
    while (n) { freq[n % 10]++; n /= 10; }
    for (int i = 0; i < 10; i++) out[i] = (char)('0' + freq[i]);
    out[10] = '\0';
}

bool reorderedPowerOf2(int n) {
    char target[11], cur[11];
    sig(n, target);
    for (int i = 0; i < 31; i++) {
        sig(1 << i, cur);
        if (strcmp(target, cur) == 0) return true;
    }
    return false;
}
