// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

var longestCommonPrefix = function(words, k) {
    const lcpOf = (a) => {
        if (!a.length) return 0;
        let pref = a[0];
        for (let t = 1; t < a.length; t++) {
            const s = a[t];
            let i = 0;
            while (i < pref.length && i < s.length && pref[i] === s[i]) i++;
            pref = pref.substring(0, i);
            if (!pref.length) return 0;
        }
        return pref.length;
    };
    const n = words.length;
    const ans = new Array(n);
    for (let i = 0; i < n; i++) {
        const rest = [];
        for (let j = 0; j < n; j++) if (j !== i) rest.push(words[j]);
        if (rest.length < k) { ans[i] = 0; continue; }
        rest.sort();
        let best = 0;
        for (let j = 0; j + k - 1 < rest.length; j++) {
            best = Math.max(best, lcpOf(rest.slice(j, j + k)));
        }
        ans[i] = best;
    }
    return ans;
};
