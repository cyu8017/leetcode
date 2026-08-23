// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue {
    constructor() {
        this.inputStack = [];
        this.outputStack = [];
    }

    _move() {
        if (this.outputStack.length === 0) {
            while (this.inputStack.length > 0) {
                this.outputStack.push(this.inputStack.pop());
            }
        }
    }

    /**
     * @param {number} x
     * @return {null}
     */
    push(x) {
        this.inputStack.push(x);
        return null;
    }

    /**
     * @return {number}
     */
    pop() {
        this._move();
        return this.outputStack.pop();
    }

    /**
     * @return {number}
     */
    peek() {
        this._move();
        return this.outputStack[this.outputStack.length - 1];
    }

    /**
     * @return {boolean}
     */
    empty() {
        return this.inputStack.length === 0 && this.outputStack.length === 0;
    }
}

module.exports = { MyQueue };
