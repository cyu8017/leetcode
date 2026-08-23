// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

class MaxStack {
    constructor() {
        this.stack = [];
        this.maxes = [];
    }

    /**
     * @param {number} x
     * @return {void}
     */
    push(x) {
        this.stack.push(x);
        this.maxes.push(this.maxes.length === 0 ? x : Math.max(x, this.maxes[this.maxes.length - 1]));
    }

    /**
     * @return {number}
     */
    pop() {
        this.maxes.pop();
        return this.stack.pop();
    }

    /**
     * @return {number}
     */
    top() { return this.stack[this.stack.length - 1]; }

    /**
     * @return {number}
     */
    peekMax() { return this.maxes[this.maxes.length - 1]; }

    /**
     * @return {number}
     */
    popMax() {
        const maxVal = this.peekMax();
        const buffer = [];
        while (this.top() !== maxVal) buffer.push(this.pop());
        this.pop();
        for (let i = buffer.length - 1; i >= 0; i--) this.push(buffer[i]);
        return maxVal;
    }
}
