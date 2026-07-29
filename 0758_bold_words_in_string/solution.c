// LeetCode 0758 - Bold Words in String
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char* boldWords(char** words, int wordsSize, char* s) {
    int n = (int)strlen(s);
    bool* bold = (bool*)calloc((size_t)n, sizeof(bool));
    for (int w = 0; w < wordsSize; w++) {
        int wlen = (int)strlen(words[w]);
        for (int start = 0; start <= n - wlen; start++) {
            if (strncmp(s + start, words[w], (size_t)wlen) == 0) {
                for (int i = start; i < start + wlen; i++) bold[i] = true;
            }
        }
    }
    char* out = (char*)malloc((size_t)n * 8 + 8);
    int pos = 0, i = 0;
    while (i < n) {
        if (bold[i]) {
            out[pos++]='*'; out[pos++]='*';
            while (i < n && bold[i]) out[pos++] = s[i++];
            out[pos++]='*'; out[pos++]='*';
        } else out[pos++] = s[i++];
    }
    out[pos] = '\0';
    free(bold);
    return out;
}
