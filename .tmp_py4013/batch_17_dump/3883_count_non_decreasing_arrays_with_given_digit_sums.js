// LeetCode 3883 - Count Non Decreasing Arrays With Given Digit Sums
// https://leetcode.com/problems/count-non-decreasing-arrays-with-given-digit-sums/

var countNonDecreasingArrays = function(digitSum) {
    const mod = 1000000007;
    const groups = Array.from({length: 51}, () => []);
    for (let x = 0; x <= 5000; x++) {
        let s = 0;
        for (let y = x; y > 0; y = Math.floor(y / 10)) s += y % 10;
        groups[s].push(x);
    }
    let prevVals = groups[digitSum[0]];
    let dp = new Array(prevVals.length).fill(1);
    for (let pos = 1; pos < digitSum.length; pos++) {
        const curVals = groups[digitSum[pos]];
        const next = new Array(curVals.length).fill(0);
        let j = 0, prefix = 0;
        for (let i = 0; i < curVals.length; i++) {
            const x = curVals[i];
            while (j < prevVals.length && prevVals[j] <= x) {
                prefix += dp[j];
                if (prefix >= mod) prefix -= mod;
                j++;
            }
            next[i] = prefix;
        }
        prevVals = curVals;
        dp = next;
    }
    let ans = 0;
    for (const x of dp) {
        ans += x;
        if (ans >= mod) ans -= mod;
    }
    return ans;
};
