// LeetCode 3532 - Path Existence Queries in a Graph I
// https://leetcode.com/problems/path-existence-queries-in-a-graph-i/

var pathExistenceQueries = function(n, nums, maxDiff, queries) {
    const g = new Array(n).fill(0);
    let cnt = 0;
    for (let i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] > maxDiff) cnt++;
        g[i] = cnt;
    }
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++)
        ans[i] = g[queries[i][0]] === g[queries[i][1]];
    return ans;
};
