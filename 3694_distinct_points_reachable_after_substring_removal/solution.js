// LeetCode 3694 - Distinct Points Reachable After Substring Removal
// https://leetcode.com/problems/distinct-points-reachable-after-substring-removal/

var distinctPoints = function(s, k) {
    const n = s.length;
    const f = new Array(n + 1).fill(0);
    const g = new Array(n + 1).fill(0);
    let x = 0, y = 0;
    for (let i = 1; i <= n; i++) {
        const c = s[i - 1];
        if (c === 'U') y++;
        else if (c === 'D') y--;
        else if (c === 'L') x--;
        else x++;
        f[i] = x;
        g[i] = y;
    }
    const st = new Set();
    for (let i = k; i <= n; i++) {
        const a = f[n] - (f[i] - f[i - k]);
        const b = g[n] - (g[i] - g[i - k]);
        st.add(a + ',' + b);
    }
    return st.size;
};
