// LeetCode 3167 - Better Compression of String
// https://leetcode.com/problems/better-compression-of-string/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* betterCompression(char* compressed) {
    int cnt[26] = {0};
    int n = (int)strlen(compressed);
    for (int i = 0; i < n; ) {
        char c = compressed[i];
        int j = i + 1, x = 0;
        while (j < n && compressed[j] >= '0' && compressed[j] <= '9') {
            x = x * 10 + (compressed[j] - '0');
            j++;
        }
        cnt[c - 'a'] += x;
        i = j;
    }
    char* ans = malloc(26 * 12 + 1);
    int p = 0;
    for (int c = 0; c < 26; c++) {
        if (cnt[c] > 0) {
            ans[p++] = 'a' + c;
            p += sprintf(ans + p, "%d", cnt[c]);
        }
    }
    ans[p] = 0;
    return ans;
}
