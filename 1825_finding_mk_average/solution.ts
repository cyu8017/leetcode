// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

export class MKAverage {
    private readonly m: number;
    private readonly k: number;
    private readonly stream: number[] = [];

    constructor(m: number, k: number) {
        this.m = m;
        this.k = k;
    }

    addElement(num: number): null {
        this.stream.push(num);
        return null;
    }

    calculateMKAverage(): number {
        if (this.stream.length < this.m) return -1;
        const window = this.stream.slice(-this.m).sort((a, b) => a - b);
        const middle = window.slice(this.k, window.length - this.k);
        let sum = 0;
        for (const v of middle) sum += v;
        return Math.floor(sum / middle.length);
    }
}
