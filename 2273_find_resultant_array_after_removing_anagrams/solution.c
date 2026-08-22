// LeetCode 2273 - Find Resultant Array After Removing Anagrams
// https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static void sig(char* w, int* c) {
    memset(c, 0, 26 * sizeof(int));
    for (int i = 0; w[i]; i++) c[w[i] - 'a']++;
}

static bool same_sig(int* a, int* b) {
    for (int i = 0; i < 26; i++) if (a[i] != b[i]) return false;
    return true;
}

char** removeAnagrams(char** words, int wordsSize, int* returnSize) {
    char** ans = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int prev[26], cur[26];
    sig(words[0], prev);
    ans[0] = words[0];
    int n = 1;
    for (int i = 1; i < wordsSize; i++) {
        sig(words[i], cur);
        if (!same_sig(cur, prev)) {
            ans[n++] = words[i];
            memcpy(prev, cur, sizeof(prev));
        }
    }
    *returnSize = n;
    return ans;
}
