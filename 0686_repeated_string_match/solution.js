// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

/**
 * @param {string} a
 * @param {string} b
 * @return {number}
 */
var repeatedStringMatch = function(a, b) {
    const repeats = Math.floor((b.length + a.length - 1) / a.length);
    let built = '';
    for (let i = 0; i < repeats; i++) built += a;
    if (built.includes(b)) return repeats;
    built += a;
    if (built.includes(b)) return repeats + 1;
    return -1;
};
