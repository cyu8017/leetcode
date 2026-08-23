// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

/**
 * @param {Function} callback
 * @param {Object} context
 * @return {void}
 */
Array.prototype.forEach = function(callback, context) {
    for (let i = 0; i < this.length; i++) {
        callback.call(context, this[i], i, this);
    }
};
