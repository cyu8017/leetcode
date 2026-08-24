// LeetCode 3039 - Apply Operations to Make String Empty
// https://leetcode.com/problems/apply-operations-to-make-string-empty/

export function lastNonEmptyString(s: any): any {
    const cnt = new Array(26).fill(0), last = new Array(26).fill(0);
    let mx = 0;
    for (let i = 0; i < s.length; i++) {
        const c = s.charCodeAt(i) - 97;
        cnt[c]++;
        last[c] = i;
        mx = Math.max(mx, cnt[c]);
    }
    let ans = '';
    for (let i = 0; i < s.length; i++) {
        const c = s.charCodeAt(i) - 97;
        if (cnt[c] === mx && last[c] === i) ans += s[i];
    }
    return ans;
}
