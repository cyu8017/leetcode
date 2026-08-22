// LeetCode 3775 - Reverse Words With Same Vowel Count
// https://leetcode.com/problems/reverse-words-with-same-vowel-count/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static int vowel_count(const char* w, int len) {
    int cnt = 0;
    for (int i = 0; i < len; i++) {
        char c = (char)tolower((unsigned char)w[i]);
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') cnt++;
    }
    return cnt;
}

char* reverseWords(char* s) {
    int n = (int)strlen(s);
    char* out = (char*)malloc((size_t)n + 2);
    int oi = 0;
    int i = 0;
    while (i < n && s[i] == ' ') i++;
    int first = 1;
    int target = -1;
    while (i < n) {
        while (i < n && s[i] == ' ') i++;
        if (i >= n) break;
        int start = i;
        while (i < n && s[i] != ' ') i++;
        int len = i - start;
        char* word = (char*)malloc((size_t)len + 1);
        memcpy(word, s + start, (size_t)len);
        word[len] = '\0';
        int vc = vowel_count(word, len);
        if (first) {
            target = vc;
            first = 0;
        } else if (vc == target) {
            for (int l = 0, r = len - 1; l < r; l++, r--) {
                char t = word[l]; word[l] = word[r]; word[r] = t;
            }
        }
        if (oi > 0) out[oi++] = ' ';
        memcpy(out + oi, word, (size_t)len);
        oi += len;
        free(word);
    }
    out[oi] = '\0';
    return out;
}
