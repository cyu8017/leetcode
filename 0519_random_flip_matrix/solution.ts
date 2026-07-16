// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

let uniform: (a: number, b: number) => number = () => 0;

export function set_uniform(uniformFn: (a: number, b: number) => number): void {
    uniform = uniformFn;
}

export function setUniform(uniformFn: (a: number, b: number) => number): void {
    uniform = uniformFn;
}

export class Solution {
    private cols: number;
    private total: number;
    private available: number[];

    constructor(m: number, n: number) {
        this.cols = n;
        this.total = m * n;
        this.available = [];
        this.reset();
    }

    flip(): number[] {
        let index = Math.trunc(uniform(0, this.available.length - 1));
        if (index >= this.available.length) index = this.available.length - 1;
        const value = this.available[index];
        this.available[index] = this.available[this.available.length - 1];
        this.available.pop();
        return [Math.floor(value / this.cols), value % this.cols];
    }

    reset(): void {
        this.available = Array.from({ length: this.total }, (_, i) => i);
    }
}
