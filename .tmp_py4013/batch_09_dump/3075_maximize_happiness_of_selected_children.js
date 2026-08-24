// LeetCode 3075 - Maximize Happiness of Selected Children
// https://leetcode.com/problems/maximize-happiness-of-selected-children/

/**
 * @param {number[]} happiness
 * @param {number} k
 * @return {number}
 */
var maximumHappinessSum = function(happiness, k) {
    happiness.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < k; i++) {
        const x = happiness[happiness.length - i - 1] - i;
        ans += Math.max(x, 0);
    }
    return ans;
};
