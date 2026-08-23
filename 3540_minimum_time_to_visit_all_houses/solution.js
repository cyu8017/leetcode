// LeetCode 3540 - Minimum Time to Visit All Houses
// https://leetcode.com/problems/minimum-time-to-visit-all-houses/

var minTotalTime = function(forward, backward, queries) {
    const n = forward.length;
    let sumB = 0;
    for (const v of backward) sumB += v;
    const pf = new Array(n + 1).fill(0), pb = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) {
        pf[i + 1] = pf[i] + forward[i];
        pb[i + 1] = pb[i] + backward[i];
    }
    let ans = 0, pos = 0;
    for (const q of queries) {
        let r = 0;
        if (q < pos) r = pf[n];
        r += pf[q] - pf[pos];
        let l = 0;
        if (q > pos) l = sumB;
        l += pb[pos] - pb[q];
        ans += Math.min(l, r);
        pos = q;
    }
    return ans;
};
