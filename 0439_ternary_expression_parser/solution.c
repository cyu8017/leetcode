// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

#include <stdlib.h>
#include <string.h>

static char* parseRange(char* expression, int start, int end) {
    int length = end - start;
    if (memchr(expression + start, '?', (size_t)length) == NULL) {
        char* result = (char*)malloc((size_t)length + 1);
        memcpy(result, expression + start, (size_t)length);
        result[length] = '\0';
        return result;
    }

    int separator = start + 2;
    int depth = 0;
    for (int index = start + 2; index < end; index++) {
        if (expression[index] == '?') {
            depth++;
        } else if (expression[index] == ':') {
            if (depth == 0) {
                separator = index;
                break;
            }
            depth--;
        }
    }

    if (expression[start] == 'T') {
        return parseRange(expression, start + 2, separator);
    }
    return parseRange(expression, separator + 1, end);
}

char* parseTernary(char* expression) {
    return parseRange(expression, 0, (int)strlen(expression));
}
