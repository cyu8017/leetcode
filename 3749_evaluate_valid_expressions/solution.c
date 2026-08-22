// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

#include <string.h>
#include <stdlib.h>
#include <ctype.h>

static const char* expr;
static int elen;

static long long parseAt(int i, int* next);

static long long parseAt(int i, int* next) {
    if ((expr[i] >= '0' && expr[i] <= '9') || expr[i] == '-') {
        int j = i;
        if (expr[j] == '-') j++;
        while (j < elen && expr[j] >= '0' && expr[j] <= '9') j++;
        char buf[32];
        int len = j - i;
        memcpy(buf, expr + i, (size_t)len);
        buf[len] = 0;
        *next = j;
        return atoll(buf);
    }
    int j = i;
    while (expr[j] != '(') j++;
    char op[8];
    int olen = j - i;
    memcpy(op, expr + i, (size_t)olen);
    op[olen] = 0;
    j++;
    int n1;
    long long val1 = parseAt(j, &n1);
    j = n1 + 1;
    int n2;
    long long val2 = parseAt(j, &n2);
    j = n2 + 1;
    long long res = 0;
    if (strcmp(op, "add") == 0) res = val1 + val2;
    else if (strcmp(op, "sub") == 0) res = val1 - val2;
    else if (strcmp(op, "mul") == 0) res = val1 * val2;
    else if (strcmp(op, "div") == 0) res = val1 / val2;
    *next = j;
    return res;
}

long long evaluateExpression(char* expression) {
    expr = expression;
    elen = (int)strlen(expression);
    int next;
    return parseAt(0, &next);
}
