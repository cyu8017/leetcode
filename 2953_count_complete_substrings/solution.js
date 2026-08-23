// LeetCode 2953 - Count Complete Substrings
// https://leetcode.com/problems/count-complete-substrings/

var countCompleteSubstrings = function(word, k) {
    const n = word.length;
    let ans = 0;
    for (let i = 0; i < n; ) {
        let j = i;
        while (j + 1 < n && Math.abs(word.charCodeAt(j + 1) - word.charCodeAt(j)) <= 2) j++;
        const seg = word.substring(i, j + 1);
        const m = seg.length;
        for (let chars = 1; chars <= 26; chars++) {
            const length = chars * k;
            if (length > m) break;
            const freq = new Array(26).fill(0);
            let unique = 0;
            for (let r = 0; r < m; r++) {
                const c = seg.charCodeAt(r) - 97;
                freq[c]++;
                if (freq[c] === 1) unique++;
                if (r >= length) {
                    const c2 = seg.charCodeAt(r - length) - 97;
                    freq[c2]--;
                    if (freq[c2] === 0) unique--;
                }
                if (r >= length - 1 && unique === chars) {
                    let ok = true;
                    for (const f of freq)
                        if (f !== 0 && f !== k) { ok = false; break; }
                    if (ok) ans++;
                }
            }
        }
        i = j + 1;
    }
    return ans;
};
