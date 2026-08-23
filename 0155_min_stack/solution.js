// LeetCode 0155 - Min Stack
// https://leetcode.com/problems/min-stack/

class MinStack {
    constructor() {
        this.stack = [];
        this.minimums = [];
    }

    /**
     * @param {number} val
     * @return {null}
     */
    push(val) {
        this.stack.push(val);
        const currentMinimum = this.minimums.length === 0
            ? val
            : Math.min(val, this.minimums[this.minimums.length - 1]);
        this.minimums.push(currentMinimum);
        return null;
    }

    /**
     * @return {null}
     */
    pop() {
        this.stack.pop();
        this.minimums.pop();
        return null;
    }

    /**
     * @return {number}
     */
    top() {
        return this.stack[this.stack.length - 1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.minimums[this.minimums.length - 1];
    }
}

module.exports = { MinStack };