"use strict";
// LeetCode 1720 - Decode XORed Array
// https://leetcode.com/problems/decode-xored-array/
function decode(encoded, first) {
    const ans = [first];
    for (const value of encoded) {
        ans.push(ans[ans.length - 1] ^ value);
    }
    return ans;
}
