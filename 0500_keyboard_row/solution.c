// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

#include <ctype.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool inRow(const char* row, char letter) {
    for (const char* cursor = row; *cursor; cursor++) {
        if (*cursor == letter) {
            return true;
        }
    }
    return false;
}

static bool onOneRow(const char* word) {
    static const char* rows[3] = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
    bool seen[256] = {false};
    for (const char* cursor = word; *cursor; cursor++) {
        if (isalpha((unsigned char)*cursor)) {
            seen[(unsigned char)tolower((unsigned char)*cursor)] = true;
        }
    }
    for (int rowIndex = 0; rowIndex < 3; rowIndex++) {
        bool subset = true;
        for (int letter = 'a'; letter <= 'z'; letter++) {
            if (!seen[letter]) {
                continue;
            }
            if (!inRow(rows[rowIndex], (char)letter)) {
                subset = false;
                break;
            }
        }
        if (subset) {
            return true;
        }
    }
    return false;
}

char** findWords(char** words, int wordsSize, int* returnSize) {
    char** result = (char**)malloc((size_t)wordsSize * sizeof(char*));
    int count = 0;
    for (int index = 0; index < wordsSize; index++) {
        if (onOneRow(words[index])) {
            result[count++] = strdup(words[index]);
        }
    }
    *returnSize = count;
    return result;
}
