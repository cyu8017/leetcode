// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

#include <stdlib.h>
#include <string.h>

int evalRPN(char **tokens, int tokensSize) {
    int *stack = malloc(tokensSize * sizeof(*stack));
    int size = 0;

    for (int i = 0; i < tokensSize; ++i) {
        char *token = tokens[i];
        if (strlen(token) == 1 && strchr("+-*/", token[0])) {
            int right = stack[--size];
            int left = stack[--size];
            switch (token[0]) {
                case '+': stack[size++] = left + right; break;
                case '-': stack[size++] = left - right; break;
                case '*': stack[size++] = left * right; break;
                default: stack[size++] = left / right; break;
            }
        } else {
            stack[size++] = atoi(token);
        }
    }
    int result = stack[0];
    free(stack);
    return result;
}
// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

void solve() {
}