"use strict";
// LeetCode 1381 - Design A Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/
class CustomStack {
    constructor(maxSize) {
        this.maxSize = maxSize;
        this.a = [];
    }
    push(x) {
        if (this.a.length < this.maxSize)
            this.a.push(x);
    }
    pop() {
        return this.a.length ? this.a.pop() : -1;
    }
    increment(k, val) {
        for (let i = 0; i < Math.min(k, this.a.length); i++)
            this.a[i] += val;
    }
}
