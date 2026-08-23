// LeetCode 3534 - Path Existence Queries in a Graph II
// https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/

var pathExistenceQueries = function(n, nums, maxDiff, queries) {
    const pairs = Array.from({length: n}, (_, i) => [nums[i], i]);
    pairs.sort((a, b) => a[0] - b[0]);
    const m = 20;
    const f = Array.from({length: n}, () => new Array(m).fill(0));
    let r = n - 1;
    for (let l = n - 1; l >= 0; l--) {
        while (pairs[r][0] - pairs[l][0] > maxDiff) r--;
        const i = pairs[l][1], j = pairs[r][1];
        f[i][0] = j;
        for (let k = 1; k < m; k++) f[i][k] = f[f[i][k - 1]][k - 1];
    }
    const ans = [];
    for (const q of queries) {
        let i = q[0], j = q[1];
        if (nums[i] > nums[j]) { const tmp = i; i = j; j = tmp; }
        if (i === j) { ans.push(0); continue; }
        if (nums[i] === nums[j]) { ans.push(1); continue; }
        let d = 0;
        for (let k = m - 1; k >= 0; k--) {
            if (nums[f[i][k]] < nums[j]) {
                d |= 1 << k;
                i = f[i][k];
            }
        }
        if (nums[f[i][0]] < nums[j]) ans.push(-1);
        else ans.push(d + 1);
    }
    return ans;
};
