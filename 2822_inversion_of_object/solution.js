// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

/**
 * @param {Object|Array} obj
 * @return {Object}
 */
var invertObject = function(obj) {
    const inverted = {};
    for (const key of Object.keys(obj)) {
        const val = obj[key];
        if (val in inverted) {
            if (!Array.isArray(inverted[val])) inverted[val] = [inverted[val]];
            inverted[val].push(key);
        } else {
            inverted[val] = key;
        }
    }
    return inverted;
};
