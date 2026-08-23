// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

/**
 * @param {number[][]} bombs
 * @return {number}
 */
var maximumDetonation = function(bombs) {
    const n = bombs.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 0; i < n; i++) {
        const x1 = bombs[i][0], y1 = bombs[i][1], r1 = bombs[i][2];
        for (let j = 0; j < n; j++) {
            if (i === j) continue;
            const dx = bombs[j][0] - x1, dy = bombs[j][1] - y1;
            if (dx * dx + dy * dy <= r1 * r1) g[i].push(j);
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const vis = new Array(n).fill(false);
        const q = [i];
        vis[i] = true;
        let cnt = 0;
        while (q.length) {
            const u = q.shift();
            cnt++;
            for (const v of g[u]) if (!vis[v]) { vis[v] = true; q.push(v); }
        }
        ans = Math.max(ans, cnt);
    }
    return ans;
};
