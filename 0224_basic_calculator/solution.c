// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

#include <ctype.h>
#include <stdlib.h>

int calculate(char* s) {
    int capacity = 64;
    int size = 0;
    int* stack = (int*)malloc((size_t)capacity * sizeof(int));
    int result = 0;
    int number = 0;
    int sign = 1;

    for (int i = 0; s[i] != '\0'; ++i) {
        char ch = s[i];
        if (isdigit((unsigned char)ch)) {
            number = number * 10 + (ch - '0');
        } else if (ch == '+' || ch == '-') {
            result += sign * number;
            number = 0;
            sign = ch == '+' ? 1 : -1;
        } else if (ch == '(') {
            if (size + 2 > capacity) {
                capacity *= 2;
                stack = (int*)realloc(stack, (size_t)capacity * sizeof(int));
            }
            stack[size++] = result;
            stack[size++] = sign;
            result = 0;
            sign = 1;
        } else if (ch == ')') {
            result += sign * number;
            number = 0;
            result *= stack[--size];
            result += stack[--size];
        }
    }

    result += sign * number;
    free(stack);
    return result;
}
