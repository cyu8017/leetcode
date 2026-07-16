// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

class MyStack {
    constructor() {
        this.queue = [];
    }

    /**
     * @param {number} x
     * @return {null}
     */
    push(x) {
        this.queue.push(x);
        for (let i = 0; i < this.queue.length - 1; i += 1) {
            this.queue.push(this.queue.shift());
        }
        return null;
    }

    /**
     * @return {number}
     */
    pop() {
        return this.queue.shift();
    }

    /**
     * @return {number}
     */
    top() {
        return this.queue[0];
    }

    /**
     * @return {boolean}
     */
    empty() {
        return this.queue.length === 0;
    }
}

module.exports = { MyStack };
