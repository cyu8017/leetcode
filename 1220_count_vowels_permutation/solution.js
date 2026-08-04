// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

/**
 * @param {number} n
 * @return {number}
 */
var countVowelPermutation = function(n) {
    const mod = 1e9 + 7;
    let a = 1, e = 1, i = 1, o = 1, u = 1;
    for (let t = 0; t < n - 1; t++) {
        [a, e, i, o, u] = [(e + i + u) % mod, (a + i) % mod, (e + o) % mod, i, (i + o) % mod];
    }
    return (a + e + i + o + u) % mod;
};
