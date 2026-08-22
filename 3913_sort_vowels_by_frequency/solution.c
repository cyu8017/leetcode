// LeetCode 3913 - Sort Vowels By Frequency
// https://leetcode.com/problems/sort-vowels-by-frequency/

#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

static bool isVowel3913(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

char* sortVowels(char* s) {
    int cnt[128] = {0};
    char vowels[16];
    int vn = 0;
    for (int i = 0; s[i]; i++) {
        unsigned char c = (unsigned char)s[i];
        if (!isVowel3913(c)) continue;
        if (cnt[c] == 0) vowels[vn++] = (char)c;
        cnt[c]++;
    }
    /* sort vowels by cnt desc */
    for (int i = 0; i < vn; i++) {
        for (int j = i + 1; j < vn; j++) {
            if (cnt[(unsigned char)vowels[j]] > cnt[(unsigned char)vowels[i]]) {
                char t = vowels[i]; vowels[i] = vowels[j]; vowels[j] = t;
            }
        }
    }
    int n = (int)strlen(s);
    char* ans = malloc((size_t)n + 1);
    strcpy(ans, s);
    int i = 0;
    for (int k = 0; s[k]; k++) {
        if (!isVowel3913(s[k])) continue;
        char ch = vowels[i];
        ans[k] = ch;
        cnt[(unsigned char)ch]--;
        if (cnt[(unsigned char)ch] == 0) i++;
    }
    return ans;
}
