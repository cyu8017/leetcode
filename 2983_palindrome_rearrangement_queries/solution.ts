// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

function countPref(pre: any, i: any, j: any): any {
    const cnt = new Array(26);
    for (let k = 0; k < 26; k++) cnt[k] = pre[j + 1][k] - pre[i][k];
    return cnt;
}function subCnt(cnt1: any, cnt2: any): any {
    const cnt = new Array(26);
    for (let i = 0; i < 26; i++) {
        cnt[i] = cnt1[i] - cnt2[i];
        if (cnt[i] < 0) return null;
    }
    return cnt;
}function eqCnt(a: any, b: any): any {
    for (let i = 0; i < 26; i++) if (a[i] !== b[i]) return false;
    return true;
}function check(pre1: any, pre2: any, diff: any, a: any, b: any, c: any, d: any): any {
    if (diff[a] > 0 || diff[diff.length - 1] - diff[Math.max(b, d) + 1] > 0) return false;
    if (d <= b) return eqCnt(countPref(pre1, a, b), countPref(pre2, a, b));
    if (b < c) {
        return diff[c] - diff[b + 1] === 0 && eqCnt(countPref(pre1, a, b), countPref(pre2, a, b)) &&
               eqCnt(countPref(pre1, c, d), countPref(pre2, c, d));
    }
    const cnt1 = subCnt(countPref(pre1, a, b), countPref(pre2, a, c - 1));
    const cnt2 = subCnt(countPref(pre2, c, d), countPref(pre1, b + 1, d));
    return cnt1 !== null && cnt2 !== null && eqCnt(cnt1, cnt2);
}export function canMakePalindromeQueries(s: any, queries: any): any {
    const n = s.length;
    const m = n / 2;
    const tArr = s.substring(m).split('').reverse();
    const t = tArr.join('');
    s = s.substring(0, m);
    const pre1 = Array.from({length: m + 1}, () => new Array(26).fill(0));
    const pre2 = Array.from({length: m + 1}, () => new Array(26).fill(0));
    const diff = new Array(m + 1).fill(0);
    for (let i = 1; i <= m; i++) {
        for (let k = 0; k < 26; k++) {
            pre1[i][k] = pre1[i - 1][k];
            pre2[i][k] = pre2[i - 1][k];
        }
        pre1[i][s.charCodeAt(i - 1) - 97]++;
        pre2[i][t.charCodeAt(i - 1) - 97]++;
        diff[i] = diff[i - 1] + (s[i - 1] === t[i - 1] ? 0 : 1);
    }
    const ans = [];
    for (let i = 0; i < queries.length; i++) {
        const q = queries[i];
        const a = q[0], b = q[1];
        const c = n - 1 - q[3], d = n - 1 - q[2];
        ans.push((a <= c) ? check(pre1, pre2, diff, a, b, c, d)
                          : check(pre2, pre1, diff, c, d, a, b));
    }
    return ans;
}
