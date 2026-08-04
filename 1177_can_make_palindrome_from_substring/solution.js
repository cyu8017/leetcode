// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var canMakePaliQueries = function(s, queries) {
    const prefix = [0];
    let mask = 0;
    for (const ch of s) {
        mask ^= 1 << (ch.charCodeAt(0) - 97);
        prefix.push(mask);
    }
    return queries.map(([left, right, k]) => {
        const bits = (prefix[right + 1] ^ prefix[left]).toString(2).split('1').length - 1;
        return Math.floor(bits / 2) <= k;
    });
};
