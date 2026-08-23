// LeetCode 3900 - Longest Balanced Substring After One Swap
// https://leetcode.com/problems/longest-balanced-substring-after-one-swap/

var longestBalanced = function(s) {
    let cnt0 = 0;
    for (const c of s) if (c === '0') cnt0++;
    const cnt1 = s.length - cnt0;
    const pos = new Map();
    pos.set(0, [-1]);
    let ans = 0, pre = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') pre++;
        else pre--;
        if (!pos.has(pre)) pos.set(pre, []);
        pos.get(pre).push(i);
        ans = Math.max(ans, i - pos.get(pre)[0]);
        if (pos.has(pre - 2)) {
            const p = pos.get(pre - 2);
            if (Math.floor((i - p[0] - 2) / 2) < cnt0) ans = Math.max(ans, i - p[0]);
            else if (p.length > 1) ans = Math.max(ans, i - p[1]);
        }
        if (pos.has(pre + 2)) {
            const p = pos.get(pre + 2);
            if (Math.floor((i - p[0] - 2) / 2) < cnt1) ans = Math.max(ans, i - p[0]);
            else if (p.length > 1) ans = Math.max(ans, i - p[1]);
        }
    }
    return ans;
};
