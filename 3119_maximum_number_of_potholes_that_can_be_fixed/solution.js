// LeetCode 3119 - Maximum Number of Potholes That Can Be Fixed
// https://leetcode.com/problems/maximum-number-of-potholes-that-can-be-fixed/

/**
 * @param {string} road
 * @param {number} budget
 * @return {number}
 */
var maxPotholes = function(road, budget) {
    road = road + ".";
    const n = road.length;
    const cnt = new Array(n).fill(0);
    let k = 0, ans = 0;
    for (let i = 0; i < n; i++) {
        const c = road[i];
        if (c === 'x') k++;
        else if (k > 0) { cnt[k]++; k = 0; }
    }
    for (k = n - 1; k > 0 && budget > 0; k--) {
        const t = Math.min(Math.floor(budget / (k + 1)), cnt[k]);
        ans += t * k;
        budget -= t * (k + 1);
        cnt[k - 1] += cnt[k] - t;
    }
    return ans;
};
