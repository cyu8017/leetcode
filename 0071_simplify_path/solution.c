// LeetCode 0071 - Simplify Path
// https://leetcode.com/problems/simplify-path/

#include <stdlib.h>
#include <string.h>

char* simplifyPath(char* path) {
    char** stack = (char**)malloc(1024 * sizeof(char*));
    int top = 0;

    char* copy = (char*)malloc(strlen(path) + 1);
    strcpy(copy, path);

    char* token = strtok(copy, "/");
    while (token != NULL) {
        if (strcmp(token, "..") == 0) {
            if (top > 0) {
                top--;
            }
        } else if (strcmp(token, ".") != 0 && token[0] != '\0') {
            stack[top++] = token;
        }
        token = strtok(NULL, "/");
    }

    if (top == 0) {
        free(copy);
        free(stack);
        char* result = (char*)malloc(2);
        strcpy(result, "/");
        return result;
    }

    size_t len = 1;
    for (int i = 0; i < top; i++) {
        len += strlen(stack[i]) + 1;
    }

    char* result = (char*)malloc(len + 1);
    result[0] = '\0';
    strcat(result, "/");
    for (int i = 0; i < top; i++) {
        strcat(result, stack[i]);
        if (i < top - 1) {
            strcat(result, "/");
        }
    }

    free(copy);
    free(stack);
    return result;
}
