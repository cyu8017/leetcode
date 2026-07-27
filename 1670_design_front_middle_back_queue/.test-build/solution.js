"use strict";
// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/
Object.defineProperty(exports, "__esModule", { value: true });
exports.FrontMiddleBackQueue = void 0;
class FrontMiddleBackQueue {
    constructor() {
        this.l = [];
        this.r = [];
    }
    _bal() {
        while (this.l.length > this.r.length + 1)
            this.r.unshift(this.l.pop());
        while (this.r.length > this.l.length)
            this.l.push(this.r.shift());
    }
    pushFront(val) {
        this.l.unshift(val);
        this._bal();
        return null;
    }
    pushMiddle(val) {
        if (this.l.length > this.r.length)
            this.r.unshift(this.l.pop());
        this.l.push(val);
        return null;
    }
    pushBack(val) {
        this.r.push(val);
        this._bal();
        return null;
    }
    popFront() {
        if (!this.l.length)
            return -1;
        const v = this.l.shift();
        this._bal();
        return v;
    }
    popMiddle() {
        if (!this.l.length)
            return -1;
        const v = this.l.pop();
        this._bal();
        return v;
    }
    popBack() {
        if (!this.l.length)
            return -1;
        const v = this.r.length ? this.r.pop() : this.l.pop();
        this._bal();
        return v;
    }
}
exports.FrontMiddleBackQueue = FrontMiddleBackQueue;
