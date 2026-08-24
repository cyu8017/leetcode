// LeetCode 3323 - Minimize Connected Groups by Inserting Interval
// https://leetcode.com/problems/minimize-connected-groups-by-inserting-interval/

var minConnectedGroups = function(intervals, k) {
    intervals.sort((a, b) => a[0] - b[0]);
    const merged = [];
    for (const it of intervals) {
        if (!merged.length || it[0] > merged[merged.length - 1][1]) merged.push([it[0], it[1]]);
        else if (it[1] > merged[merged.length - 1][1]) merged[merged.length - 1][1] = it[1];
    }
    const m = merged.length;
    let ans = m;
    for (let i = 0; i < m; i++) {
        const end = merged[i][1] + k;
        let j = i;
        while (j < m && merged[j][0] <= end) j++;
        const groups = i + 1 + (m - j);
        if (groups < ans) ans = groups;
    }
    return ans;
};
