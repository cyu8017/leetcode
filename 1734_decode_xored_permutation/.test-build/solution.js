"use strict";
// LeetCode 1734 - Decode XORed Permutation
// https://leetcode.com/problems/decode-xored-permutation/
function decode(encoded) {
    const n = encoded.length + 1;
    let total = 0;
    for (let value = 1; value <= n; value++) {
        total ^= value;
    }
    let odd = 0;
    for (let i = 1; i < encoded.length; i += 2) {
        odd ^= encoded[i];
    }
    const first = total ^ odd;
    const ans = [first];
    for (const value of encoded) {
        ans.push(ans[ans.length - 1] ^ value);
    }
    return ans;
}
