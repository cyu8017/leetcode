// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isSubseq2014(const char* s, const char* t, int k) {
    int need = 0, times = 0, tn = (int)strlen(t);
    if (tn == 0) return true;
    for (int i = 0; s[i]; i++) {
        if (s[i] == t[need]) {
            need++;
            if (need == tn) {
                times++;
                if (times == k) return true;
                need = 0;
            }
        }
    }
    return false;
}

char* longestSubsequenceRepeatedK(char* s, int k) {
    int freq[26] = {0};
    for (int i = 0; s[i]; i++) freq[s[i] - 'a']++;
    char chars[26];
    int cn = 0;
    for (int c = 25; c >= 0; c--) if (freq[c] >= k) chars[cn++] = (char)('a' + c);

    char** queue = (char**)malloc(4096 * sizeof(char*));
    int qh = 0, qt = 0;
    queue[qt++] = strdup("");
    char* best = strdup("");
    while (qh < qt) {
        char* cur = queue[qh++];
        for (int i = 0; i < cn; i++) {
            int len = (int)strlen(cur);
            char* nxt = (char*)malloc((size_t)len + 2);
            memcpy(nxt, cur, (size_t)len);
            nxt[len] = chars[i];
            nxt[len + 1] = '\0';
            if (isSubseq2014(s, nxt, k)) {
                int bl = (int)strlen(best);
                if (len + 1 > bl || (len + 1 == bl && strcmp(nxt, best) > 0)) {
                    free(best);
                    best = strdup(nxt);
                }
                queue[qt++] = nxt;
            } else {
                free(nxt);
            }
        }
        free(cur);
    }
    free(queue);
    return best;
}
