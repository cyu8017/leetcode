// LeetCode 3572 - Maximize Y-Sum by Picking a Triplet of Distinct X-Values
// https://leetcode.com/problems/maximize-ysum-by-picking-a-triplet-of-distinct-xvalues/

var maxSumDistinctTriplet = function(x, y) {
    const n = x.length;
    const arr = Array.from({length: n}, (_, i) => [x[i], y[i]]);
    arr.sort((a, b) => b[1] - a[1]);
    let ans = 0;
    const vis = new Set();
    for (let i = 0; i < n; i++) {
        const a = arr[i][0], b = arr[i][1];
        if (!vis.has(a)) {
            vis.add(a);
            ans += b;
            if (vis.size === 3) return ans;
        }
    }
    return -1;
};
