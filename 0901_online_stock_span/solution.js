// LeetCode 0901 - Online Stock Span
// https://leetcode.com/problems/online-stock-span/

class StockSpanner {
    constructor() {
        this.stack = [];
    }

    /**
     * @param {number} price
     * @return {number}
     */
    next(price) {
        let span = 1;
        while (this.stack.length && this.stack[this.stack.length - 1][0] <= price) {
            span += this.stack[this.stack.length - 1][1];
            this.stack.pop();
        }
        this.stack.push([price, span]);
        return span;
    }
}

module.exports = { StockSpanner };
