// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

var maximumLength = function(s) {
    const n = s.length;
    let ans = -1;
    for (let i = 0; i < n; i++) {
        for (let j = i; j < n; j++) {
            if (s[j] !== s[i]) break;
            const len = j - i + 1;
            let cnt = 0;
            for (let k = 0; k + len <= n; k++) {
                let ok = true;
                for (let t = 0; t < len; t++) {
                    if (s[k + t] !== s[i + t]) { ok = false; break; }
                }
                if (ok) cnt++;
            }
            if (cnt >= 3 && len > ans) ans = len;
        }
    }
    return ans;
};
