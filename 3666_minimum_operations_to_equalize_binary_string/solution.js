// LeetCode 3666 - Minimum Operations to Equalize Binary String
// https://leetcode.com/problems/minimum-operations-to-equalize-binary-string/

var minOperations = function(s, k) {
    const n = s.length;
    const ts = [new Set(), new Set()];
    for (let i = 0; i <= n; i++) ts[i % 2].add(i);
    let cnt0 = 0;
    for (const c of s) if (c === '0') cnt0++;
    ts[cnt0 % 2].delete(cnt0);
    let q = [cnt0];
    let ans = 0;
    while (q.length) {
        const nq = [];
        for (const cur of q) {
            if (cur === 0) return ans;
            const l = cur + k - 2 * Math.min(cur, k);
            const r = cur + k - 2 * Math.max(k - n + cur, 0);
            const t = ts[l % 2];
            const sorted = [...t].sort((a, b) => a - b);
            for (const it of sorted) {
                if (it < l) continue;
                if (it > r) break;
                nq.push(it);
                t.delete(it);
            }
        }
        q = nq;
        ans++;
    }
    return -1;
};
