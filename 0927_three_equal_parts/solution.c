// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

#include <stdlib.h>
#include <string.h>

int* threeEqualParts(int* arr, int arrSize, int* returnSize) {
    int* ones = (int*)malloc((size_t)arrSize * sizeof(int));
    int n = 0;
    for (int i = 0; i < arrSize; i++) if (arr[i]) ones[n++] = i;
    int* ans = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;
    if (n % 3) { ans[0] = ans[1] = -1; free(ones); return ans; }
    if (n == 0) { ans[0] = 0; ans[1] = arrSize - 1; free(ones); return ans; }
    int third = n / 3;
    int length = ones[n - 1] - ones[2 * third] + 1;
    int a = ones[0], b = ones[third], c = ones[2 * third];
    if (a + length > arrSize || b + length > arrSize || c + length > arrSize ||
        memcmp(arr + a, arr + b, (size_t)length * sizeof(int)) != 0 ||
        memcmp(arr + a, arr + c, (size_t)length * sizeof(int)) != 0) {
        ans[0] = ans[1] = -1;
    } else {
        ans[0] = a + length - 1;
        ans[1] = b + length;
    }
    free(ones);
    return ans;
}
