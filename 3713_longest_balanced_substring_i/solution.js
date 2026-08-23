// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

var longestBalanced = function(s) {
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const cnt = new Array(26).fill(0);
        let mx = 0, v = 0;
        for (let j = i; j < n; j++) {
            const c = s.charCodeAt(j) - 97;
            cnt[c]++;
            if (cnt[c] === 1) v++;
            mx = Math.max(mx, cnt[c]);
            if (mx * v === j - i + 1) ans = Math.max(ans, j - i + 1);
        }
    }
    return ans;
};
