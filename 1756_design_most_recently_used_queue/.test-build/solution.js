"use strict";
// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/
Object.defineProperty(exports, "__esModule", { value: true });
exports.MRUQueue = void 0;
class MRUQueue {
    constructor(n) {
        this.q = [];
        for (let i = 1; i <= n; i++) {
            this.q.push(i);
        }
    }
    fetch(k) {
        const val = this.q.splice(k - 1, 1)[0];
        this.q.push(val);
        return val;
    }
}
exports.MRUQueue = MRUQueue;
