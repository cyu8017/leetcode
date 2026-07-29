// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

#include <stdbool.h>
#include <string.h>

bool isValid(char* code) {
    char stack[100][16];
    int top = 0;
    int i = 0;
    int n = (int)strlen(code);

    while (i < n) {
        if (strncmp(code + i, "<![CDATA[", 9) == 0) {
            if (top == 0) {
                return false;
            }
            char* end = strstr(code + i + 9, "]]>");
            if (end == NULL) {
                return false;
            }
            i = (int)(end - code) + 3;
        } else if (strncmp(code + i, "</", 2) == 0) {
            char* end = strchr(code + i + 2, '>');
            if (end == NULL) {
                return false;
            }
            int tagLen = (int)(end - (code + i + 2));
            if (top == 0 || tagLen <= 0 || tagLen > 9 || strncmp(stack[top - 1], code + i + 2, (size_t)tagLen) != 0 || stack[top - 1][tagLen] != '\0') {
                return false;
            }
            top--;
            i = (int)(end - code) + 1;
            if (top == 0 && i < n) {
                return false;
            }
        } else if (code[i] == '<') {
            char* end = strchr(code + i + 1, '>');
            if (end == NULL) {
                return false;
            }
            int tagLen = (int)(end - (code + i + 1));
            if (tagLen <= 0 || tagLen > 9) {
                return false;
            }
            for (int t = 0; t < tagLen; t++) {
                char ch = code[i + 1 + t];
                if (ch < 'A' || ch > 'Z') {
                    return false;
                }
            }
            strncpy(stack[top], code + i + 1, (size_t)tagLen);
            stack[top][tagLen] = '\0';
            top++;
            i = (int)(end - code) + 1;
        } else {
            if (top == 0) {
                return false;
            }
            i++;
        }
    }
    return top == 0;
}
