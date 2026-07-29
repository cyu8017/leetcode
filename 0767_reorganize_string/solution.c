// LeetCode 0767 - Reorganize String
#include <stdlib.h>
#include <string.h>

char* reorganizeString(char* s) {
    int cnt[26] = {0}, n = (int)strlen(s);
    for (int i = 0; i < n; i++) cnt[s[i]-'a']++;
    int maxc = 0, maxi = 0;
    for (int i = 0; i < 26; i++) if (cnt[i] > maxc) { maxc = cnt[i]; maxi = i; }
    if (maxc > (n + 1) / 2) { char* e = (char*)malloc(1); e[0]='\0'; return e; }
    char* out = (char*)malloc((size_t)n + 1);
    int idx = 0;
    while (cnt[maxi]--) { out[idx] = (char)('a' + maxi); idx += 2; if (idx >= n) idx = 1; }
    for (int c = 0; c < 26; c++) {
        while (cnt[c]-- > 0) { out[idx] = (char)('a' + c); idx += 2; if (idx >= n) idx = 1; }
    }
    out[n] = '\0';
    return out;
}
