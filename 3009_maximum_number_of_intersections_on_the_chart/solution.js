// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

var maxIntersectionCount = function(y) {
    const n = y.length;
    const line = new Map();
    for (let i = 1; i < n; i++) {
        let start = 2 * y[i - 1];
        let end = 2 * y[i];
        if (i !== n - 1) {
            if (y[i] > y[i - 1]) end--;
            else end++;
        }
        let a = start, b = end;
        if (a > b) { const t = a; a = b; b = t; }
        line.set(a, (line.get(a) || 0) + 1);
        line.set(b + 1, (line.get(b + 1) || 0) - 1);
    }
    const keys = [...line.keys()].sort((a, b) => a - b);
    let ans = 0, cur = 0;
    for (const key of keys) {
        cur += line.get(key);
        if (cur > ans) ans = cur;
    }
    return ans;
};
