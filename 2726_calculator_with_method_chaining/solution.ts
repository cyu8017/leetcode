// LeetCode 2726 - Calculator with Method Chaining
// https://leetcode.com/problems/calculator-with-method-chaining/

export class Calculator {
    constructor(value: any) {
        this.val = value;
    }
    add(value: any): any {
        this.val += value;
        return this;
    }
    subtract(value: any): any {
        this.val -= value;
        return this;
    }
    multiply(value: any): any {
        this.val *= value;
        return this;
    }
    divide(value: any): any {
        if (value === 0) throw new Error("Division by zero is not allowed");
        this.val /= value;
        return this;
    }
    power(value: any): any {
        this.val = Math.pow(this.val, value);
        return this;
    }
    getResult(): any {
        return this.val;
    }
}
