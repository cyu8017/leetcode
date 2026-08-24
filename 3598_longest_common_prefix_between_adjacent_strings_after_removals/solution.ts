// LeetCode 3598 - Longest Common Prefix Between Adjacent Strings After Removals
// https://leetcode.com/problems/longest-common-prefix-between-adjacent-strings-after-removals/

export function longestCommonPrefix(words: any): any {
    const n = words.length;
    const tm = new Map();
    const keys = [];
    function calc(s: any, t: any): any {
        const m = Math.min(s.length, t.length);
        for (let k = 0; k < m; k++) if (s[k] !== t[k]) return k;
        return m;
    }    function addKey(x: any): any {
        if (!tm.has(x)) {
            tm.set(x, 0);
            let lo = 0, hi = keys.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (keys[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            keys.splice(lo, 0, x);
        }
        tm.set(x, tm.get(x) + 1);
    }    function remKey(x: any): any {
        const c = tm.get(x) - 1;
        if (c === 0) {
            tm.delete(x);
            const ix = keys.indexOf(x);
            if (ix >= 0) keys.splice(ix, 1);
        } else tm.set(x, c);
    }    function add(i: any, j: any): any {
        if (i >= 0 && i < n && j >= 0 && j < n) addKey(calc(words[i], words[j]));
    }    function remove(i: any, j: any): any {
        if (i >= 0 && i < n && j >= 0 && j < n) remKey(calc(words[i], words[j]));
    }    for (let i = 0; i + 1 < n; i++) add(i, i + 1);
    const ans = new Array(n).fill(0);
    for (let i = 0; i < n; i++) {
        remove(i, i + 1);
        remove(i - 1, i);
        add(i - 1, i + 1);
        if (keys.length && keys[keys.length - 1] > 0) ans[i] = keys[keys.length - 1];
        remove(i - 1, i + 1);
        add(i - 1, i);
        add(i, i + 1);
    }
    return ans;
}
