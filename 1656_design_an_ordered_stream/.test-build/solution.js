"use strict";
// LeetCode 1656 - Design an Ordered Stream
// https://leetcode.com/problems/design-an-ordered-stream/
Object.defineProperty(exports, "__esModule", { value: true });
exports.OrderedStream = void 0;
class OrderedStream {
    constructor(n) {
        this.a = Array(n + 1).fill(null);
        this.p = 1;
    }
    insert(idKey, value) {
        this.a[idKey] = value;
        const out = [];
        while (this.p < this.a.length && this.a[this.p] !== null) {
            out.push(this.a[this.p]);
            this.p++;
        }
        return out;
    }
}
exports.OrderedStream = OrderedStream;
