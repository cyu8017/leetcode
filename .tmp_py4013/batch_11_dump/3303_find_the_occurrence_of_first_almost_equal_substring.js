// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

var minStartingIndex = function(s, pattern) {
    const n = s.length, m = pattern.length;
    for (let i = 0; i + m <= n; i++) {
        let diff = 0;
        for (let j = 0; j < m; j++) {
            if (s[i + j] !== pattern[j]) {
                diff++;
                if (diff > 1) break;
            }
        }
        if (diff <= 1) return i;
    }
    return -1;
};
