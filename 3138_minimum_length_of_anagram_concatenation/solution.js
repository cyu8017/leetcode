// LeetCode 3138 - Minimum Length of Anagram Concatenation
// https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

/**
 * @param {string} s
 * @return {number}
 */
var minAnagramLength = function(s) {
    const n = s.length;
    const cnt = new Array(26).fill(0);
    for (let i = 0; i < n; i++) cnt[s.charCodeAt(i) - 97]++;
    const check = (k) => {
        for (let i = 0; i < n; i += k) {
            const cnt1 = new Array(26).fill(0);
            for (let j = i; j < i + k; j++) cnt1[s.charCodeAt(j) - 97]++;
            for (let j = 0; j < 26; j++) {
                if (cnt1[j] * (n / k) !== cnt[j]) return false;
            }
        }
        return true;
    };
    for (let i = 1; ; i++) {
        if (n % i === 0 && check(i)) return i;
    }
};
