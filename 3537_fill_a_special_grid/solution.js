// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

var specialGrid = function(n) {
    const m = 1 << n;
    const ans = Array.from({length: m}, () => new Array(m).fill(0));
    let val = 0;
    function dfs(x, y, k) {
        if (k === 1) {
            ans[x][y] = val++;
            return;
        }
        const h = k >> 1;
        dfs(x, y, h);
        dfs(x + h, y, h);
        dfs(x + h, y - h, h);
        dfs(x, y - h, h);
    }
    dfs(0, m - 1, m);
    return ans;
};
