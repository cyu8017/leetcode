// LeetCode 3723 - Maximize Sum of Squares of Digits
// https://leetcode.com/problems/maximize-sum-of-squares-of-digits/

#include <stdlib.h>
#include <string.h>

char* maxSumOfSquares(int num, int sum) {
    if (num * 9 < sum) {
        char* e = (char*)malloc(1); e[0] = 0; return e;
    }
    int k = sum / 9, s = sum % 9;
    char* ans = (char*)malloc((size_t)(num + 1));
    int p = 0;
    for (int i = 0; i < k; i++) ans[p++] = '9';
    if (s > 0) ans[p++] = (char)('0' + s);
    while (p < num) ans[p++] = '0';
    ans[p] = 0;
    return ans;
}
