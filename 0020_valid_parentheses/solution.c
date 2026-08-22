// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

#include <stdbool.h>

bool isValid(char* s) {
    char stack[10000];
    int top = 0;

    for (int i = 0; s[i] != '\0'; i++) {
        char ch = s[i];
        if (ch == '(' || ch == '[' || ch == '{') {
            stack[top++] = ch;
        } else {
            if (top == 0) {
                return false;
            }
            char open = stack[--top];
            if ((ch == ')' && open != '(') ||
                (ch == ']' && open != '[') ||
                (ch == '}' && open != '{')) {
                return false;
            }
        }
    }

    return top == 0;
}
