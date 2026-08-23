// LeetCode 2655 - Find Maximal Uncovered Ranges
// https://leetcode.com/problems/find-maximal-uncovered-ranges/

var findMaximalUncoveredRanges = function(n, ranges) {
    ranges = ranges.slice().sort((a, b) => a[0] - b[0]);
    const ans = [];
    let cur = 0;
    for (const r of ranges) {
        if (r[0] > cur) ans.push([cur, r[0] - 1]);
        if (r[1] + 1 > cur) cur = r[1] + 1;
    }
    if (cur < n) ans.push([cur, n - 1]);
    return ans;
};
