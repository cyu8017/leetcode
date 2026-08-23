// LeetCode 0898 - Bitwise ORs of Subarrays
// https://leetcode.com/problems/bitwise-ors-of-subarrays/

/**
 * @param {number[]} arr
 * @return {number}
 */
var subarrayBitwiseORs = function(arr) {
    const ans = new Set();
    let cur = new Set();
    for (const x of arr) {
        const nxt = new Set([x]);
        for (const y of cur) nxt.add(x | y);
        cur = nxt;
        for (const v of cur) ans.add(v);
    }
    return ans.size;
};
