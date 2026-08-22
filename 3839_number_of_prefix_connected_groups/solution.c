// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

#include <stdlib.h>
#include <string.h>

int prefixConnected(char** words, int wordsSize, int k) {
    char** keys = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int* cnt = (int*)calloc((size_t)wordsSize, sizeof(int));
    int ksz = 0;
    for (int i = 0; i < wordsSize; i++) {
        int len = (int)strlen(words[i]);
        if (len < k) continue;
        char* pref = (char*)malloc((size_t)k + 1);
        memcpy(pref, words[i], (size_t)k);
        pref[k] = '\0';
        int found = -1;
        for (int j = 0; j < ksz; j++) if (strcmp(keys[j], pref) == 0) { found = j; break; }
        if (found >= 0) { cnt[found]++; free(pref); }
        else { keys[ksz] = pref; cnt[ksz] = 1; ksz++; }
    }
    int ans = 0;
    for (int i = 0; i < ksz; i++) {
        if (cnt[i] > 1) ans++;
        free(keys[i]);
    }
    free(keys); free(cnt);
    return ans;
}
