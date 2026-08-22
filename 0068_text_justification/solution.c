// LeetCode 0068 - Text Justification
// https://leetcode.com/problems/text-justification/

#include <stdlib.h>
#include <string.h>

static char* build_left_line(char** words, int start, int count, int maxWidth) {
    int chars = 0;
    for (int k = 0; k < count; k++) {
        chars += (int)strlen(words[start + k]);
        if (k > 0) {
            chars += 1;
        }
    }

    char* line = (char*)malloc((size_t)maxWidth + 1);
    int pos = 0;
    for (int k = 0; k < count; k++) {
        if (k > 0) {
            line[pos++] = ' ';
        }
        int len = (int)strlen(words[start + k]);
        memcpy(line + pos, words[start + k], (size_t)len);
        pos += len;
    }
    for (int k = pos; k < maxWidth; k++) {
        line[k] = ' ';
    }
    line[maxWidth] = '\0';
    return line;
}

static char* build_justified_line(char** words, int start, int count, int maxWidth) {
    int totalChars = 0;
    for (int k = 0; k < count; k++) {
        totalChars += (int)strlen(words[start + k]);
    }

    int totalSpaces = maxWidth - totalChars;
    int gaps = count - 1;
    int space = totalSpaces / gaps;
    int remainder = totalSpaces % gaps;

    char* line = (char*)malloc((size_t)maxWidth + 1);
    int pos = 0;
    for (int k = 0; k < count - 1; k++) {
        int len = (int)strlen(words[start + k]);
        memcpy(line + pos, words[start + k], (size_t)len);
        pos += len;
        int gapSpaces = space + (k < remainder ? 1 : 0);
        for (int s = 0; s < gapSpaces; s++) {
            line[pos++] = ' ';
        }
    }
    int lastLen = (int)strlen(words[start + count - 1]);
    memcpy(line + pos, words[start + count - 1], (size_t)lastLen);
    pos += lastLen;
    line[pos] = '\0';
    return line;
}

char** fullJustify(char** words, int wordsSize, int maxWidth, int* returnSize) {
    int capacity = 16;
    char** result = (char**)malloc((size_t)capacity * sizeof(char*));
    *returnSize = 0;

    int i = 0;
    while (i < wordsSize) {
        int lineStart = i;
        int lineCount = 0;
        int lineLen = 0;

        while (i < wordsSize) {
            int extra = lineCount > 0 ? 1 : 0;
            int wordLen = (int)strlen(words[i]);
            if (lineLen + wordLen + extra > maxWidth) {
                break;
            }
            lineCount++;
            lineLen += wordLen + extra;
            i++;
        }

        char* line;
        if (i == wordsSize || lineCount == 1) {
            line = build_left_line(words, lineStart, lineCount, maxWidth);
        } else {
            line = build_justified_line(words, lineStart, lineCount, maxWidth);
        }

        if (*returnSize >= capacity) {
            capacity *= 2;
            result = (char**)realloc(result, (size_t)capacity * sizeof(char*));
        }
        result[*returnSize] = line;
        (*returnSize)++;
    }

    result = (char**)realloc(result, (size_t)(*returnSize) * sizeof(char*));
    return result;
}
