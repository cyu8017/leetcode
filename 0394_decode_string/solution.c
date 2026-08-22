// LeetCode 0394 - Decode String
// https://leetcode.com/problems/decode-string/

#include <ctype.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* text;
    int count;
} StackEntry;

static char* duplicateString(const char* source, int repeat) {
    size_t length = strlen(source);
    char* result = (char*)malloc((size_t)repeat * length + 1);
    char* write = result;

    for (int index = 0; index < repeat; index++) {
        memcpy(write, source, length + 1);
        write += length;
    }
    return result;
}

static char* concatStrings(const char* left, const char* right) {
    size_t leftLength = strlen(left);
    size_t rightLength = strlen(right);
    char* result = (char*)malloc(leftLength + rightLength + 1);
    memcpy(result, left, leftLength);
    memcpy(result + leftLength, right, rightLength + 1);
    return result;
}

char* decodeString(char* s) {
    StackEntry* stack = NULL;
    int stackSize = 0;
    int stackCapacity = 0;
    char current[100005];
    current[0] = '\0';
    int number = 0;

    for (int index = 0; s[index] != '\0'; index++) {
        char ch = s[index];
        if (isdigit((unsigned char)ch)) {
            number = number * 10 + (ch - '0');
        } else if (ch == '[') {
            if (stackSize == stackCapacity) {
                stackCapacity = stackCapacity == 0 ? 4 : stackCapacity * 2;
                stack = (StackEntry*)realloc(stack, (size_t)stackCapacity * sizeof(StackEntry));
            }
            stack[stackSize].text = strdup(current);
            stack[stackSize].count = number;
            stackSize += 1;
            current[0] = '\0';
            number = 0;
        } else if (ch == ']') {
            stackSize -= 1;
            StackEntry entry = stack[stackSize];
            char* repeated = duplicateString(current, entry.count);
            char* merged = concatStrings(entry.text, repeated);
            free(entry.text);
            free(repeated);
            strcpy(current, merged);
            free(merged);
        } else {
            size_t length = strlen(current);
            current[length] = ch;
            current[length + 1] = '\0';
        }
    }

    free(stack);
    return strdup(current);
}
