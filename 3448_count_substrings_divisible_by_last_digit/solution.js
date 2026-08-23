// LeetCode 3448 - Count Substrings Divisible By Last Digit
// https://leetcode.com/problems/count-substrings-divisible-by-last-digit/

var countSubstrings = function(s) {
    let ans = 0;
    const n = s.length;
    for (let r = 0; r < n; r++) {
        const last = s.charCodeAt(r) - 48;
        if (last === 0) continue;
        let mod = 0;
        let p = 1 % last;
        for (let l = r; l >= 0; l--) {
            mod = (mod + (s.charCodeAt(l) - 48) * p) % last;
            p = (p * 10) % last;
            if (mod === 0) ans++;
        }
    }
    return ans;
};
