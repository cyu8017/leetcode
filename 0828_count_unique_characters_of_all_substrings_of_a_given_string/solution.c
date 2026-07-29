// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

#include <string.h>
#include <stdlib.h>

int uniqueLetterString(char* s) {
    int n = (int)strlen(s);
    int* idx[26];
    int cnt[26] = {0};
    int cap[26];
    for (int i = 0; i < 26; i++) {
        cap[i] = 8;
        idx[i] = (int*)malloc((size_t)cap[i] * sizeof(int));
        idx[i][cnt[i]++] = -1;
    }
    for (int i = 0; i < n; i++) {
        int c = s[i] - 'A';
        if (cnt[c] + 1 >= cap[c]) {
            cap[c] *= 2;
            idx[c] = (int*)realloc(idx[c], (size_t)cap[c] * sizeof(int));
        }
        idx[c][cnt[c]++] = i;
    }
    int ans = 0;
    for (int c = 0; c < 26; c++) {
        if (cnt[c] + 1 >= cap[c]) {
            cap[c] *= 2;
            idx[c] = (int*)realloc(idx[c], (size_t)cap[c] * sizeof(int));
        }
        idx[c][cnt[c]++] = n;
        for (int k = 1; k < cnt[c] - 1; k++)
            ans += (idx[c][k] - idx[c][k - 1]) * (idx[c][k + 1] - idx[c][k]);
        free(idx[c]);
    }
    return ans;
}
