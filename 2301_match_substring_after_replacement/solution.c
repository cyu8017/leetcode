// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

#include <stdbool.h>
#include <string.h>

bool matchReplacement(char* s, char* sub, char** mappings, int mappingsSize, int* mappingsColSize) {
    (void)mappingsColSize;
    bool allow[128][128];
    memset(allow, 0, sizeof(allow));
    for (int i = 0; i < mappingsSize; i++) {
        allow[(unsigned char)mappings[i][0]][(unsigned char)mappings[i][1]] = true;
    }
    int n = (int)strlen(s), m = (int)strlen(sub);
    for (int i = 0; i + m <= n; i++) {
        bool ok = true;
        for (int j = 0; j < m; j++) {
            unsigned char a = (unsigned char)s[i + j];
            unsigned char b = (unsigned char)sub[j];
            if (a == b || allow[b][a]) continue;
            ok = false;
            break;
        }
        if (ok) return true;
    }
    return false;
}
