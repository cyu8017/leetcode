// LeetCode 2106 - Maximum Fruits Harvested After at Most K Steps
// https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

/**
 * @param {number[][]} fruits
 * @param {number} startPos
 * @param {number} k
 * @return {number}
 */
var maxTotalFruits = function(fruits, startPos, k) {
    const minSteps = (left, right, start) => {
        if (right <= start) return start - left;
        if (left >= start) return right - start;
        return Math.min((start - left) + (right - left), (right - start) + (right - left));
    };
    const n = fruits.length;
    const pref = new Array(n + 1).fill(0);
    const pos = new Array(n);
    for (let i = 0; i < n; i++) {
        pos[i] = fruits[i][0];
        pref[i + 1] = pref[i] + fruits[i][1];
    }
    let ans = 0, j = 0;
    for (let i = 0; i < n; i++) {
        while (j < n && minSteps(pos[i], pos[j], startPos) > k) j++;
        if (j <= i) ans = Math.max(ans, pref[i + 1] - pref[j]);
    }
    j = 0;
    for (let i = 0; i < n; i++) {
        while (j <= i && minSteps(pos[j], pos[i], startPos) > k) j++;
        ans = Math.max(ans, pref[i + 1] - pref[j]);
    }
    return ans;
};
