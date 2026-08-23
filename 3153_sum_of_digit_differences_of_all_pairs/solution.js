// LeetCode 3153 - Sum of Digit Differences of All Pairs
// https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumDigitDifferences = function(nums) {
    const n = nums.length;
    const m = Math.floor(Math.log10(nums[0])) + 1;
    let ans = 0;
    const vals = nums.slice();
    for (let k = 0; k < m; k++) {
        const cnt = new Array(10).fill(0);
        for (let i = 0; i < n; i++) {
            cnt[vals[i] % 10]++;
            vals[i] = Math.floor(vals[i] / 10);
        }
        for (const v of cnt) ans += v * (n - v);
    }
    return ans / 2;
};
