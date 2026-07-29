// LeetCode 1592 - Rearrange Spaces Between Words
// https://leetcode.com/problems/rearrange-spaces-between-words/

#include <stdlib.h>
#include <string.h>

char* reorderSpaces(char* text) {
    int n = (int)strlen(text);
    int spaces = 0, wordCount = 0;
    char** words = (char**)malloc((size_t)(n + 1) * sizeof(char*));
    int i = 0;
    while (i < n) {
        if (text[i] == ' ') {
            spaces++;
            i++;
            continue;
        }
        int start = i;
        while (i < n && text[i] != ' ') i++;
        int len = i - start;
        words[wordCount] = (char*)malloc((size_t)len + 1);
        memcpy(words[wordCount], text + start, (size_t)len);
        words[wordCount][len] = '\0';
        wordCount++;
    }
    char* out = (char*)malloc((size_t)n + 1);
    int pos = 0;
    if (wordCount == 1) {
        int len = (int)strlen(words[0]);
        memcpy(out, words[0], (size_t)len);
        pos = len;
        for (int s = 0; s < spaces; s++) out[pos++] = ' ';
    } else {
        int between = spaces / (wordCount - 1);
        int trailing = spaces % (wordCount - 1);
        for (int w = 0; w < wordCount; w++) {
            int len = (int)strlen(words[w]);
            memcpy(out + pos, words[w], (size_t)len);
            pos += len;
            int gap = (w + 1 < wordCount) ? between : trailing;
            for (int s = 0; s < gap; s++) out[pos++] = ' ';
        }
    }
    out[pos] = '\0';
    for (int w = 0; w < wordCount; w++) free(words[w]);
    free(words);
    return out;
}
