// LeetCode 3839 - Number Of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

var prefixConnected = function(words, k) {
    const cnt = new Map();
    for (const w of words) {
        if (w.length >= k) {
            const p = w.substring(0, k);
            cnt.set(p, (cnt.get(p) || 0) + 1);
        }
    }
    let ans = 0;
    for (const v of cnt.values()) if (v > 1) ans++;
    return ans;
};
