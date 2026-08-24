// LeetCode 3951 - Minimum Energy To Maintain Brightness
// https://leetcode.com/problems/minimum-energy-to-maintain-brightness/

var minEnergy = function(n, brightness, intervals) {
    intervals.sort((a, b) => a[0] - b[0]);
    const merged = [];
    merged.push([intervals[0][0], intervals[0][1]]);
    for (let i = 1; i < intervals.length; i++) {
        const x = intervals[i];
        const last = merged[merged.length - 1];
        if (last[1] < x[0]) merged.push([x[0], x[1]]);
        else if (x[1] > last[1]) last[1] = x[1];
    }
    let ans = 0;
    for (const interval of merged) {
        const m = interval[1] - interval[0] + 1;
        ans += Math.floor((brightness + 2) / 3) * m;
    }
    return ans;
};
