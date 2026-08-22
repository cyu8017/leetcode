// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

#include <stdlib.h>
#include <string.h>

char* mergeCharacters(char* s, int k) {
    int last[256];
    for (int i = 0; i < 256; i++) last[i] = -1;
    int n = (int)strlen(s);
    char* ans = (char*)malloc((size_t)n + 1);
    int cur = 0;
    for (int i = 0; i < n; i++) {
        unsigned char c = (unsigned char)s[i];
        if (last[c] != -1 && cur - last[c] <= k) continue;
        ans[cur] = (char)c;
        last[c] = cur;
        cur++;
    }
    ans[cur] = '\0';
    return ans;
}
