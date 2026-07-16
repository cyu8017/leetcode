// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

#include <ctype.h>
#include <stdlib.h>

int calculate(char* s) {
    int capacity = 32;
    int size = 0;
    int* stack = malloc((size_t)capacity * sizeof(int));
    int number = 0;
    char operator = '+';

    for (int index = 0; s[index] != '\0'; index++) {
        char ch = s[index];
        if (isdigit((unsigned char)ch)) {
            number = number * 10 + (ch - '0');
        }
        if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || s[index + 1] == '\0') {
            if (operator == '+') {
                if (size == capacity) {
                    capacity *= 2;
                    stack = realloc(stack, (size_t)capacity * sizeof(int));
                }
                stack[size++] = number;
            } else if (operator == '-') {
                if (size == capacity) {
                    capacity *= 2;
                    stack = realloc(stack, (size_t)capacity * sizeof(int));
                }
                stack[size++] = -number;
            } else if (operator == '*') {
                stack[size - 1] = stack[size - 1] * number;
            } else if (operator == '/') {
                stack[size - 1] = stack[size - 1] / number;
            }
            operator = ch;
            number = 0;
        }
    }

    int total = 0;
    for (int i = 0; i < size; i++) {
        total += stack[i];
    }
    free(stack);
    return total;
}
