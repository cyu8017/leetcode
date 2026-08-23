// LeetCode 2285 - Maximum Total Importance of Roads
// https://leetcode.com/problems/maximum-total-importance-of-roads/

var maximumImportance = function(n, roads) {
    const deg = new Array(n).fill(0);
    for (const r of roads) { deg[r[0]]++; deg[r[1]]++; }
    deg.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < n; i++) ans += deg[i] * (i + 1);
    return ans;
};
