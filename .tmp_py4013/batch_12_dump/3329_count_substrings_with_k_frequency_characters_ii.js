// LeetCode 3329 - Count Substrings With K-Frequency Characters II
// https://leetcode.com/problems/count-substrings-with-k-frequency-characters-ii/

var numberOfSubstrings = function(s, k) {
    const n = s.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const freq = new Array(26).fill(0);
        for (let j = i; j < n; j++) {
            freq[s.charCodeAt(j) - 97]++;
            let ok = false;
            for (const f of freq) if (f >= k) { ok = true; break; }
            if (ok) { ans += n - j; break; }
        }
    }
    return ans;
};
