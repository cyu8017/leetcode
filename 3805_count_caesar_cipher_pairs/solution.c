// LeetCode 3805 - Count Caesar Cipher Pairs
// https://leetcode.com/problems/count-caesar-cipher-pairs/

#include <stdlib.h>
#include <string.h>

typedef struct { char* key; int cnt; } Entry3805;

long long countPairs(char** words, int wordsSize) {
    Entry3805* cnt = (Entry3805*)calloc((size_t)wordsSize, sizeof(Entry3805));
    int csz = 0;
    for (int wi = 0; wi < wordsSize; wi++) {
        char* s = words[wi];
        int len = (int)strlen(s);
        char* t = (char*)malloc((size_t)len + 1);
        memcpy(t, s, (size_t)len + 1);
        int k = 'z' - t[0];
        for (int i = 1; i < len; i++) t[i] = (char)('a' + (t[i] - 'a' + k) % 26);
        t[0] = 'z';
        int found = -1;
        for (int i = 0; i < csz; i++) if (strcmp(cnt[i].key, t) == 0) { found = i; break; }
        if (found >= 0) { cnt[found].cnt++; free(t); }
        else { cnt[csz].key = t; cnt[csz].cnt = 1; csz++; }
    }
    long long ans = 0;
    for (int i = 0; i < csz; i++) {
        long long v = cnt[i].cnt;
        ans += v * (v - 1) / 2;
        free(cnt[i].key);
    }
    free(cnt);
    return ans;
}
