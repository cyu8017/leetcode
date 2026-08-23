// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

/**
 * @param {number} n
 * @return {number}
 */
var nextBeautifulNumber = function(n) {
    const balanced = (x) => {
        const cnt = new Array(10).fill(0);
        while (x > 0) { cnt[x % 10]++; x = Math.floor(x / 10); }
        for (let d = 0; d < 10; d++) if (cnt[d] !== 0 && cnt[d] !== d) return false;
        return true;
    };
    for (let x = n + 1; ; x++) if (balanced(x)) return x;
};
