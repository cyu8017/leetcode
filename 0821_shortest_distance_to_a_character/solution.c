// LeetCode 0821 - Shortest Distance to a Character
// https://leetcode.com/problems/shortest-distance-to-a-character/

#include <stdlib.h>
#include <string.h>

#define MIN(a,b) ((a)<(b)?(a):(b))

int* shortestToChar(char* s, char c, int* returnSize) {
    int n = (int)strlen(s);
    int* ans = (int*)malloc((size_t)n * sizeof(int));
    int prev = -n;
    for (int i = 0; i < n; i++) {
        if (s[i] == c) prev = i;
        ans[i] = i - prev;
    }
    prev = 2 * n;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == c) prev = i;
        ans[i] = MIN(ans[i], prev - i);
    }
    *returnSize = n;
    return ans;
}
