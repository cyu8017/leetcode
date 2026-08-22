// LeetCode 2489 - Number of Substrings With Fixed Ratio
// https://leetcode.com/problems/number-of-substrings-with-fixed-ratio/

#include <stdlib.h>
#include <string.h>

long long fixedRatio(char* s, int num1, int num2) {
    int n = (int)strlen(s);
    int cap = 1;
    while (cap < n * 2 + 16) cap <<= 1;
    int* keys = (int*)malloc((size_t)cap * sizeof(int));
    int* vals = (int*)calloc((size_t)cap, sizeof(int));
    char* used = (char*)calloc((size_t)cap, 1);
    {
        int key0 = 0;
        unsigned h = (unsigned)key0 * 2654435761u;
        int idx = (int)(h & (unsigned)(cap - 1));
        keys[idx] = 0;
        used[idx] = 1;
        vals[idx] = 1;
    }
    int zeros = 0, ones = 0;
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '0') zeros++; else ones++;
        int key = zeros * num2 - ones * num1;
        unsigned h = (unsigned)key * 2654435761u;
        int idx = (int)(h & (unsigned)(cap - 1));
        while (used[idx] && keys[idx] != key) idx = (idx + 1) & (cap - 1);
        ans += vals[idx];
        keys[idx] = key;
        used[idx] = 1;
        vals[idx]++;
    }
    free(keys); free(vals); free(used);
    return ans;
}
