// LeetCode 2619 - Array Prototype Last
// https://leetcode.com/problems/array-prototype-last/

/**
 * @return {null|boolean|number|string|Array|Object}
 */
Array.prototype.last = function() {
    if (this.length === 0) return -1;
    return this[this.length - 1];
};
