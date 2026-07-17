// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/

/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    const ans = [first];
    for (const value of encoded) {
        ans.push(ans[ans.length - 1] ^ value);
    }
    return ans;
};
