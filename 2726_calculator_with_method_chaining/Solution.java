// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

class Calculator {
    private double val;

    public Calculator(double v) {
        val = v;
    }

    public Calculator add(double v) {
        val += v;
        return this;
    }

    public Calculator subtract(double v) {
        val -= v;
        return this;
    }

    public Calculator multiply(double v) {
        val *= v;
        return this;
    }

    public Calculator divide(double v) {
        if (v != 0) val /= v;
        return this;
    }

    public Calculator power(double v) {
        val = Math.pow(val, v);
        return this;
    }

    public double getResult() {
        return val;
    }
}

class Solution {
    public Calculator calculatorCreate(double val) {
        return new Calculator(val);
    }
}
