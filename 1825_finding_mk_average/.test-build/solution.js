"use strict";
// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/
Object.defineProperty(exports, "__esModule", { value: true });
exports.MKAverage = void 0;
class MKAverage {
    constructor(m, k) {
        this.stream = [];
        this.m = m;
        this.k = k;
    }
    addElement(num) {
        this.stream.push(num);
        return null;
    }
    calculateMKAverage() {
        if (this.stream.length < this.m)
            return -1;
        const window = this.stream.slice(-this.m).sort((a, b) => a - b);
        const middle = window.slice(this.k, window.length - this.k);
        let sum = 0;
        for (const v of middle)
            sum += v;
        return Math.floor(sum / middle.length);
    }
}
exports.MKAverage = MKAverage;
