// LeetCode 0791 - Custom Sort String
#include <stdlib.h>
#include <string.h>

char* customSortString(char* order, char* s) {
    int cnt[26] = {0};
    for (char* p = s; *p; p++) cnt[*p - 'a']++;
    char* out = (char*)malloc(strlen(s) + 1);
    int pos = 0;
    for (char* p = order; *p; p++) {
        while (cnt[*p - 'a']-- > 0) out[pos++] = *p;
        cnt[*p - 'a'] = 0;
    }
    for (int c = 0; c < 26; c++) while (cnt[c]-- > 0) out[pos++] = (char)('a' + c);
    out[pos] = '\0';
    return out;
}
