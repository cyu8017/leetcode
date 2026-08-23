// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/

/**
 * @param {Array<Function>} functions
 * @param {number} ms
 * @return {Array<Function>}
 */
var delayAll = function(functions, ms) {
    return functions.map((fn) => {
        return async function() {
            try {
                const result = await fn();
                await new Promise((r) => setTimeout(r, ms));
                return result;
            } catch (err) {
                await new Promise((r) => setTimeout(r, ms));
                throw err;
            }
        };
    });
};
