// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* addBoldTag(char* s, char** words, int wordsSize) {
    int n = (int)strlen(s);
    bool* bold = (bool*)calloc((size_t)n, sizeof(bool));
    for (int w = 0; w < wordsSize; w++) {
        int len = (int)strlen(words[w]);
        if (len == 0) {
            continue;
        }
        for (int i = 0; i + len <= n; i++) {
            if (strncmp(s + i, words[w], (size_t)len) == 0) {
                for (int j = i; j < i + len; j++) {
                    bold[j] = true;
                }
            }
        }
    }
    char* result = (char*)malloc((size_t)n * 8 + 1);
    int pos = 0;
    int i = 0;
    while (i < n) {
        if (bold[i]) {
            memcpy(result + pos, "<b>", 3);
            pos += 3;
            while (i < n && bold[i]) {
                result[pos++] = s[i++];
            }
            memcpy(result + pos, "</b>", 4);
            pos += 4;
        } else {
            result[pos++] = s[i++];
        }
    }
    result[pos] = '\0';
    free(bold);
    return result;
}
