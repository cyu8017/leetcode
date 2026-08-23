// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

/**
 * @param {string} num
 * @return {boolean}
 */
var isStrobogrammatic = function(num) {
    const mapping = {0: "0", 1: "1", 6: "9", 8: "8", 9: "6"};
    let left = 0;
    let right = num.length - 1;
    while (left <= right) {
        if (mapping[num[left]] !== num[right]) {
            return false;
        }
        left += 1;
        right -= 1;
    }
    return true;
};
