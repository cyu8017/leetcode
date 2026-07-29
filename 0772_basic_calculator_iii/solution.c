// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

#include <ctype.h>
#include <string.h>

static int parseCalc(const char* expr, int* i, int n) {
    int stack[400];
    int top = 0;
    long long num = 0;
    char sign = '+';
    while (*i < n) {
        char ch = expr[*i];
        if (isdigit((unsigned char)ch)) {
            num = num * 10 + (ch - '0');
        }
        if (ch == '(') {
            (*i)++;
            num = parseCalc(expr, i, n);
            ch = (*i < n) ? expr[*i] : ')';
        }
        if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' || *i == n - 1) {
            if (sign == '+') {
                stack[top++] = (int)num;
            } else if (sign == '-') {
                stack[top++] = (int)(-num);
            } else if (sign == '*') {
                stack[top - 1] *= (int)num;
            } else {
                int a = stack[--top];
                stack[top++] = (int)(a / (double)num);
            }
            if (ch == ')') {
                break;
            }
            sign = ch;
            num = 0;
        }
        (*i)++;
    }
    int sum = 0;
    for (int k = 0; k < top; k++) {
        sum += stack[k];
    }
    return sum;
}

int calculate(char* s) {
    char buf[400];
    int n = 0;
    for (char* p = s; *p; p++) {
        if (*p != ' ') {
            buf[n++] = *p;
        }
    }
    int i = 0;
    return parseCalc(buf, &i, n);
}
