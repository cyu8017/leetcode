// LeetCode 1090 - Largest Values From Labels
// https://leetcode.com/problems/largest-values-from-labels/

/**
 * @param {number[]} values
 * @param {number[]} labels
 * @param {number} numWanted
 * @param {number} useLimit
 * @return {number}
 */
var largestValsFromLabels = function(values, labels, numWanted, useLimit) {
    const items = values.map((v, i) => [v, labels[i]]).sort((a, b) => b[0] - a[0]);
    const used = new Map();
    let ans = 0;
    let taken = 0;
    for (const [value, label] of items) {
        if (taken === numWanted) break;
        const cnt = used.get(label) || 0;
        if (cnt < useLimit) {
            used.set(label, cnt + 1);
            ans += value;
            taken++;
        }
    }
    return ans;
};
