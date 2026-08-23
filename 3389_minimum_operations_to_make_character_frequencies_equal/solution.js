// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

var makeStringGood = function(s) {
    const freq = new Array(26).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 97]++;
    let ans = s.length;
    for (let t = 1; t <= s.length; t++) {
        let pool = 0;
        for (let i = 0; i < 26; i++) if (freq[i] > t) pool += freq[i] - t;
        let deficit = 0;
        for (let i = 0; i < 26; i++) if (freq[i] < t) deficit += t - freq[i];
        const ops = Math.max(pool, deficit);
        if (ops < ans) ans = ops;
    }
    if (s.length < ans) ans = s.length;
    return ans;
};
