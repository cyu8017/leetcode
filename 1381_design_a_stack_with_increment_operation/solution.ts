// LeetCode 1381 - Design A Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack {
    a: any;
    maxSize: any;
    constructor(maxSize: number) {

        this.maxSize = maxSize;
        this.a = [];
    }
    push(x: number): void {

        if (this.a.length < this.maxSize) this.a.push(x);
    }
    pop(): number {

        return this.a.length ? this.a.pop() : -1;
    }
    increment(k: number, val: number): void {

        for (let i = 0; i < Math.min(k, this.a.length); i++) this.a[i] += val;
    }
}
