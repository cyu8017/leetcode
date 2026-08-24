// LeetCode 4001 - Aggregate Two Time Series
// https://leetcode.com/problems/aggregate-two-time-series/

var aggregateTimeSeries = function(series1, series2) {
    const m = series1.length, n = series2.length;
    let i = 0, j = 0;
    const ans = [];
    while (i < m && j < n) {
        const t1 = series1[i][0], v1 = series1[i][1];
        const t2 = series2[j][0], v2 = series2[j][1];
        if (t1 === t2) {
            ans.push([t1, v1 + v2]);
            i++;
            j++;
        } else if (t1 < t2) {
            ans.push([t1, v1 + v2]);
            i++;
        } else {
            ans.push([t2, v1 + v2]);
            j++;
        }
    }
    while (i < m) {
        ans.push([series1[i][0], series1[i][1]]);
        i++;
    }
    while (j < n) {
        ans.push([series2[j][0], series2[j][1]]);
        j++;
    }
    return ans;
};
