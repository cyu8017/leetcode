// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static void parse(const char* expr, int* coef, int* constant) {
    *coef = 0;
    *constant = 0;
    int i = 0;
    int n = (int)strlen(expr);
    while (i < n) {
        int sign = 1;
        if (expr[i] == '+' || expr[i] == '-') {
            if (expr[i] == '-') {
                sign = -1;
            }
            i++;
        }
        int value = 0;
        int hasDigit = 0;
        while (i < n && expr[i] >= '0' && expr[i] <= '9') {
            hasDigit = 1;
            value = value * 10 + (expr[i] - '0');
            i++;
        }
        if (i < n && expr[i] == 'x') {
            if (!hasDigit) {
                value = 1;
            }
            *coef += sign * value;
            i++;
        } else {
            *constant += sign * value;
        }
    }
}

char* solveEquation(char* equation) {
    char* eq = strchr(equation, '=');
    int leftLen = (int)(eq - equation);
    char left[256], right[256];
    memcpy(left, equation, (size_t)leftLen);
    left[leftLen] = '\0';
    strcpy(right, eq + 1);
    int lc, lk, rc, rk;
    parse(left, &lc, &lk);
    parse(right, &rc, &rk);
    int coef = lc - rc;
    int constant = rk - lk;
    char* result = (char*)malloc(64);
    if (coef == 0) {
        strcpy(result, constant == 0 ? "Infinite solutions" : "No solution");
    } else {
        snprintf(result, 64, "x=%d", constant / coef);
    }
    return result;
}
