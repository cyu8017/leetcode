// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

export class MaxStack {
    constructor() {
        this.stack = [];
        this.maxes = [];
    }

    push(x: any): any {
        this.stack.push(x);
        this.maxes.push(this.maxes.length === 0 ? x : Math.max(x, this.maxes[this.maxes.length - 1]));
    }

    pop(): any {
        this.maxes.pop();
        return this.stack.pop();
    }

    top(): any { return this.stack[this.stack.length - 1]; }

    peekMax(): any { return this.maxes[this.maxes.length - 1]; }

    popMax(): any {
        const maxVal = this.peekMax();
        const buffer = [];
        while (this.top() !== maxVal) buffer.push(this.pop());
        this.pop();
        for (let i = buffer.length - 1; i >= 0; i--) this.push(buffer[i]);
        return maxVal;
    }
}
