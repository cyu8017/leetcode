// LeetCode 2268 - Minimum Number of Keypresses
// https://leetcode.com/problems/minimum-number-of-keypresses/

/**
 * @param {string} s
 * @return {number}
 */
var minimumKeypresses = function(s) {
    const freq = new Array(26).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 97]++;
    freq.sort((a, b) => b - a);
    let ans = 0;
    for (let i = 0; i < 26; i++) {
        if (freq[i] === 0) break;
        ans += freq[i] * (Math.floor(i / 9) + 1);
    }
    return ans;
};
