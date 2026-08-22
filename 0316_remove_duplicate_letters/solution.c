// LeetCode 0316 - Remove Duplicate Letters
// https://leetcode.com/problems/remove-duplicate-letters/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char* removeDuplicateLetters(char* s) {
    int length = (int)strlen(s);
    int lastIndex[256];
    bool seen[256];
    for (int index = 0; index < 256; index++) {
        lastIndex[index] = -1;
        seen[index] = false;
    }
    for (int index = 0; index < length; index++) {
        lastIndex[(unsigned char)s[index]] = index;
    }

    char* stack = (char*)malloc((size_t)length + 1);
    int stackSize = 0;

    for (int index = 0; index < length; index++) {
        unsigned char character = (unsigned char)s[index];
        if (seen[character]) {
            continue;
        }
        while (stackSize > 0
            && (unsigned char)stack[stackSize - 1] > character
            && lastIndex[(unsigned char)stack[stackSize - 1]] > index) {
            seen[(unsigned char)stack[stackSize - 1]] = false;
            stackSize -= 1;
        }
        stack[stackSize++] = (char)character;
        seen[character] = true;
    }

    stack[stackSize] = '\0';
    return stack;
}
