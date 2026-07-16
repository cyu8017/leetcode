// LeetCode 0155 - Min Stack
// https://leetcode.com/problems/min-stack/

export class MinStack {
    private readonly stack: number[] = [];
    private readonly minimums: number[] = [];

    push(val: number): null {
        this.stack.push(val);
        const currentMinimum = this.minimums.length === 0
            ? val
            : Math.min(val, this.minimums[this.minimums.length - 1]);
        this.minimums.push(currentMinimum);
        return null;
    }

    pop(): null {
        this.stack.pop();
        this.minimums.pop();
        return null;
    }

    top(): number {
        return this.stack[this.stack.length - 1];
    }

    getMin(): number {
        return this.minimums[this.minimums.length - 1];
    }
}