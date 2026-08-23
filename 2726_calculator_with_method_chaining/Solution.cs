// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

using System;

public class Calculator {
    double val;
    public Calculator(double v) { val = v; }
    public Calculator Add(double v) { val += v; return this; }
    public Calculator Subtract(double v) { val -= v; return this; }
    public Calculator Multiply(double v) { val *= v; return this; }
    public Calculator Divide(double v) { if (v != 0) val /= v; return this; }
    public Calculator Power(double v) { val = Math.Pow(val, v); return this; }
    public double GetResult() => val;
}

public class Solution {
    public Calculator CalculatorCreate(double val) => new Calculator(val);
}
