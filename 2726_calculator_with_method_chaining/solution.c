// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

#include <stdlib.h>
#include <math.h>

typedef struct {
    double val;
} Calculator;

Calculator* calculatorCreate(double val) {
    Calculator* c = (Calculator*)malloc(sizeof(Calculator));
    c->val = val;
    return c;
}

Calculator* calculatorAdd(Calculator* c, double v) { c->val += v; return c; }
Calculator* calculatorSubtract(Calculator* c, double v) { c->val -= v; return c; }
Calculator* calculatorMultiply(Calculator* c, double v) { c->val *= v; return c; }
Calculator* calculatorDivide(Calculator* c, double v) {
    if (v == 0) return c;
    c->val /= v;
    return c;
}
Calculator* calculatorPower(Calculator* c, double v) {
    c->val = pow(c->val, v);
    return c;
}
double calculatorGetResult(Calculator* c) { return c->val; }
void calculatorFree(Calculator* c) { free(c); }
