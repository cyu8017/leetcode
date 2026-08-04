// LeetCode 1381 - Design A Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

/**
 * @param {number} maxSize
 */
var CustomStack = function(maxSize) {
    this.maxSize = maxSize;
    this.a = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
CustomStack.prototype.push = function(x) {
    if (this.a.length < this.maxSize) this.a.push(x);
};

/**
 * @return {number}
 */
CustomStack.prototype.pop = function() {
    return this.a.length ? this.a.pop() : -1;
};

/** 
 * @param {number} k 
 * @param {number} val
 * @return {void}
 */
CustomStack.prototype.increment = function(k, val) {
    for (let i = 0; i < Math.min(k, this.a.length); i++) this.a[i] += val;
};
