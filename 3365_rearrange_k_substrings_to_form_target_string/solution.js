// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

var isPossibleToRearrange = function(s, t, k) {
    const n = s.length;
    const sz = Math.floor(n / k);
    const cnt = new Map();
    for (let i = 0; i < n; i += sz) {
        const a = s.substring(i, i + sz), b = t.substring(i, i + sz);
        cnt.set(a, (cnt.get(a) || 0) + 1);
        cnt.set(b, (cnt.get(b) || 0) - 1);
    }
    for (const v of cnt.values()) if (v !== 0) return false;
    return true;
};
