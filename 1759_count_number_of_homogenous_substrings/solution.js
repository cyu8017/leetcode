// LeetCode 1759 - Count Number of Homogenous Substrings
// https://leetcode.com/problems/count-number-of-homogenous-substrings/

/**
 * @param {string} s
 * @return {number}
 */
var countHomogenous = function(s) {
    const MOD = 1000000007;
    let ans = 0;
    let i = 0;
    while (i < s.length) {
        let j = i;
        while (j < s.length && s[j] === s[i]) {
            j++;
        }
        const length = j - i;
        ans = (ans + (length * (length + 1)) / 2) % MOD;
        i = j;
    }
    return ans;
};
