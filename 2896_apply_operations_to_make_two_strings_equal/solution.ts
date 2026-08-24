// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

export function minOperations(s1: string, s2: string, x: number): number {
    const diff = [];
    for (let i = 0; i < s1.length; i++) if (s1[i] !== s2[i]) diff.push(i);
    const m = diff.length;
    if (m % 2 === 1) return -1;
    if (m === 0) return 0;
    const INF = 1 << 30;
    const dp2 = Array(m + 1).fill(INF);
    dp2[0] = 0;
    for (let i = 0; i < m; i++) {
        if (dp2[i] >= INF) continue;
        if (i + 1 < m) {
            let cand = diff[i + 1] - diff[i];
            if (cand > x) cand = x;
            if (dp2[i] + cand < dp2[i + 2]) dp2[i + 2] = dp2[i] + cand;
        }
    }
    return dp2[m] >= INF ? -1 : dp2[m];
}
