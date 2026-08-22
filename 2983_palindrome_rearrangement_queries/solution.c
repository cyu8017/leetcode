// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* canMakePalindromeQueries(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = (int)strlen(s);
    int half = n / 2;
    bool* ans = (bool*)malloc((size_t)queriesSize * sizeof(bool));
    bool* mark = (bool*)malloc((size_t)n * sizeof(bool));
    for (int qi = 0; qi < queriesSize; qi++) {
        int a = queries[qi][0], b = queries[qi][1], c = queries[qi][2], d = queries[qi][3];
        memset(mark, 0, (size_t)n * sizeof(bool));
        for (int i = a; i <= b; i++) mark[i] = true;
        for (int i = c; i <= d; i++) mark[i] = true;
        int freq[26] = {0};
        bool ok = true;
        for (int i = 0; i < half; i++) {
            int j = n - 1 - i;
            if (!mark[i] && !mark[j]) {
                if (s[i] != s[j]) { ok = false; break; }
            } else {
                if (mark[i]) freq[s[i] - 'a']++;
                else freq[s[i] - 'a']--;
                if (mark[j]) freq[s[j] - 'a']++;
                else freq[s[j] - 'a']--;
            }
        }
        if (ok) {
            for (int f = 0; f < 26; f++) {
                if (freq[f] != 0) { ok = false; break; }
            }
        }
        ans[qi] = ok;
    }
    free(mark);
    *returnSize = queriesSize;
    return ans;
}
