// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

/**
 * @param {number[]} nums
 * @return {number}
 */
var countBeautifulPairs = function(nums) {
    const gcd = (a, b) => {
        while (b) { const t = a % b; a = b; b = t; }
        return a;
    };
    const firstDigit = (x) => {
        while (x >= 10) x = Math.floor(x / 10);
        return x;
    };
    let ans = 0;
    const freq = Array(10).fill(0);
    for (const x of nums) {
        const last = x % 10;
        for (let d = 1; d <= 9; d++)
            if (freq[d] > 0 && gcd(d, last) === 1) ans += freq[d];
        freq[firstDigit(x)]++;
    }
    return ans;
};
