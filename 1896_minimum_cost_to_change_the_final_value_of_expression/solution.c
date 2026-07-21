// LeetCode 1896 - Minimum Cost to Change the Final Value of Expression
// https://leetcode.com/problems/minimum-cost-to-change-the-final-value-of-expression/

#include <string.h>

typedef struct {
    int val;
    int toZero;
    int toOne;
} Node;

static char* g_expr;
static int g_index;

static int min3(int a, int b, int c) {
    int m = a < b ? a : b;
    return m < c ? m : c;
}

static Node combine(Node left, char op, Node right) {
    Node out;
    if (op == '&') {
        int andToZero = left.toZero < left.toOne + right.toZero ? left.toZero : left.toOne + right.toZero;
        int andToOne = left.toOne + right.toOne;
        int orToZero = left.toZero + right.toZero;
        int orToOne = min3(left.toOne, left.toZero + right.toOne, right.toZero + left.toOne);
        out.val = left.val & right.val;
        out.toZero = andToZero < 1 + orToZero ? andToZero : 1 + orToZero;
        out.toOne = andToOne < 1 + orToOne ? andToOne : 1 + orToOne;
    } else {
        int orToZero = left.toZero + right.toZero;
        int orToOne = min3(left.toOne, left.toZero + right.toOne, right.toZero + left.toOne);
        int andToZero = left.toZero < left.toOne + right.toZero ? left.toZero : left.toOne + right.toZero;
        int andToOne = left.toOne + right.toOne;
        out.val = left.val | right.val;
        out.toZero = orToZero < 1 + andToZero ? orToZero : 1 + andToZero;
        out.toOne = orToOne < 1 + andToOne ? orToOne : 1 + andToOne;
    }
    return out;
}

static Node parseExpr(void);

static Node parseFactor(void) {
    if (g_expr[g_index] == '0' || g_expr[g_index] == '1') {
        int value = g_expr[g_index++] - '0';
        Node node = {value, value == 0 ? 0 : 1, value == 0 ? 1 : 0};
        return node;
    }
    g_index++;
    Node node = parseExpr();
    g_index++;
    return node;
}

static Node parseExpr(void) {
    Node node = parseFactor();
    while (g_expr[g_index] == '&' || g_expr[g_index] == '|') {
        char op = g_expr[g_index++];
        node = combine(node, op, parseFactor());
    }
    return node;
}

int minOperationsToFlip(char* expression) {
    g_expr = expression;
    g_index = 0;
    Node node = parseExpr();
    return node.val ? node.toZero : node.toOne;
}
