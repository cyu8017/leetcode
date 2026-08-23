// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

#include <cmath>

class Calculator {
    double val;
public:
    Calculator(double v) : val(v) {}
    Calculator& add(double v) { val += v; return *this; }
    Calculator& subtract(double v) { val -= v; return *this; }
    Calculator& multiply(double v) { val *= v; return *this; }
    Calculator& divide(double v) { if (v != 0) val /= v; return *this; }
    Calculator& power(double v) { val = std::pow(val, v); return *this; }
    double getResult() const { return val; }
};

// ensure non-stub file also exposes Solution for harnesses that look for it
class Solution {
public:
    Calculator CalculatorCreate(double val) { return Calculator(val); }
};
