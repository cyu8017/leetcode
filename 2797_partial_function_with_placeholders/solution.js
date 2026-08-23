// LeetCode 2797 - Partial Function with Placeholders
// https://leetcode.com/problems/partial-function-with-placeholders/

/**
 * @param {Function} fn
 * @param {Array} args
 * @return {Function}
 */
var partial = function(fn, args) {
    return function(...restArgs) {
        const full = [];
        let ri = 0;
        for (const a of args) {
            if (a === '_') {
                if (ri < restArgs.length) full.push(restArgs[ri++]);
            } else {
                full.push(a);
            }
        }
        while (ri < restArgs.length) full.push(restArgs[ri++]);
        return fn(...full);
    };
};
