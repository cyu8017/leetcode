// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

/**
 * @param {number[]} reward1
 * @param {number[]} reward2
 * @param {number} k
 * @return {number}
 */
var miceAndCheese = function(reward1, reward2, k) {
    const n = reward1.length;
    const diff = new Array(n);
    let ans = 0;
    for (let i = 0; i < n; ++i) {
        ans += reward2[i];
        diff[i] = reward1[i] - reward2[i];
    }
    diff.sort((a, b) => b - a);
    for (let i = 0; i < k; ++i) ans += diff[i];
    return ans;
};
