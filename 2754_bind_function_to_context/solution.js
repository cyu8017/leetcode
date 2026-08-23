// LeetCode 2754 - Bind Function to Context
// https://leetcode.com/problems/bind-function-to-context/

/**
 * @param {Object} obj
 * @return {Function}
 */
Function.prototype.bindPolyfill = function(obj) {
    const fn = this;
    return function(...args) {
        return fn.apply(obj, args);
    };
};
