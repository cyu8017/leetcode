// LeetCode 0677 - Map Sum Pairs
// https://leetcode.com/problems/map-sum-pairs/

var MapSum = function() {
    this.values = new Map();
    this.prefixSums = new Map();
};

/**
 * @param {string} key
 * @param {number} val
 * @return {void}
 */
MapSum.prototype.insert = function(key, val) {
    const delta = val - (this.values.get(key) || 0);
    this.values.set(key, val);
    for (let i = 1; i <= key.length; ++i) {
        const prefix = key.substring(0, i);
        this.prefixSums.set(prefix, (this.prefixSums.get(prefix) || 0) + delta);
    }
};

/**
 * @param {string} prefix
 * @return {number}
 */
MapSum.prototype.sum = function(prefix) {
    return this.prefixSums.get(prefix) || 0;
};
