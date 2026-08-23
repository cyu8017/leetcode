// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

/**
 * @param {string} s
 * @return {number}
 */
var minimumSubstringsInPartition = function(s) {
    const n = s.length;
    const memo = new Array(n).fill(-1);
    const dfs = (i) => {
        if (i >= n) return 0;
        if (memo[i] !== -1) return memo[i];
        const cnt = new Array(26).fill(0);
        const freq = new Map();
        memo[i] = n - i;
        for (let j = i; j < n; j++) {
            const k = s.charCodeAt(j) - 97;
            if (cnt[k] > 0) {
                const c = cnt[k];
                const nv = freq.get(c) - 1;
                if (nv === 0) freq.delete(c);
                else freq.set(c, nv);
            }
            cnt[k]++;
            freq.set(cnt[k], (freq.get(cnt[k]) || 0) + 1);
            if (freq.size === 1) {
                memo[i] = Math.min(memo[i], 1 + dfs(j + 1));
            }
        }
        return memo[i];
    };
    return dfs(0);
};
