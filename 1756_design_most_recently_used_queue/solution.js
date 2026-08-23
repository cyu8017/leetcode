// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

/**
 * @param {number} n
 */
var MRUQueue = function(n) {
    this.q = [];
    for (let i = 1; i <= n; i++) {
        this.q.push(i);
    }
};

/**
 * @param {number} k
 * @return {number}
 */
MRUQueue.prototype.fetch = function(k) {
    const val = this.q.splice(k - 1, 1)[0];
    this.q.push(val);
    return val;
};
