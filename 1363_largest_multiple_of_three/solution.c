// LeetCode 1363 - Largest Multiple of Three
// https://leetcode.com/problems/largest-multiple-of-three/

#include <stdlib.h>
#include <string.h>

static int remove_rem(int* cnt, int r, int k) {
    for (int d = r; d < 10; d += 3) {
        while (cnt[d] && k) { cnt[d]--; k--; }
        if (!k) return 1;
    }
    return 0;
}

char* largestMultipleOfThree(int* digits, int digitsSize) {
    int cnt[10] = {0}, sum = 0;
    for (int i = 0; i < digitsSize; i++) { cnt[digits[i]]++; sum += digits[i]; }
    int rem = sum % 3;
    if (rem && !remove_rem(cnt, rem, 1)) remove_rem(cnt, 3 - rem, 2);
    char* s = (char*)malloc(digitsSize + 1);
    int len = 0;
    for (int d = 9; d >= 0; d--)
        for (int i = 0; i < cnt[d]; i++) s[len++] = '0' + d;
    s[len] = '\0';
    if (len && s[0] == '0') { s[0] = '0'; s[1] = '\0'; }
    return s;
}
