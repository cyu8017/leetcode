// LeetCode 2002 - Maximum Product of the Length of Two Palindromic Subsequences
// https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/

/**
 * @param {string} s
 * @return {number}
 */
var maxProduct = function(s) {
    const palLen = (mask) => {
        let chars = "";
        for (let i = 0; i < s.length; i++)
            if ((mask & (1 << i)) !== 0) chars += s[i];
        for (let l = 0, r = chars.length - 1; l < r; l++, r--)
            if (chars[l] !== chars[r]) return 0;
        return chars.length;
    };
    const n = s.length;
    let best = 0;
    const total = 1 << n;
    for (let mask1 = 1; mask1 < total; mask1++) {
        const len1 = palLen(mask1);
        if (len1 === 0) continue;
        const remain = (total - 1) ^ mask1;
        for (let mask2 = remain; mask2 > 0; mask2 = (mask2 - 1) & remain) {
            const len2 = palLen(mask2);
            if (len2 > 0 && len1 * len2 > best) best = len1 * len2;
        }
    }
    return best;
};
