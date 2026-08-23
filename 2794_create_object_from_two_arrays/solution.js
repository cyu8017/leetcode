// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

/**
 * @param {Array} keysArr
 * @param {Array} valuesArr
 * @return {Object}
 */
var createObject = function(keysArr, valuesArr) {
    const output = {};
    const n = Math.min(keysArr.length, valuesArr.length);
    for (let i = 0; i < n; i++) {
        if (!(keysArr[i] in output)) output[keysArr[i]] = valuesArr[i];
    }
    return output;
};
