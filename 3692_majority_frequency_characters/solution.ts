// LeetCode 3692 - Majority Frequency Characters
// https://leetcode.com/problems/majority-frequency-characters/

export function majorityFrequencyGroup(s: any): any {
    const cnt = new Array(26).fill(0);
    for (const c of s) cnt[c.charCodeAt(0) - 97]++;
    const f = new Map();
    for (let i = 0; i < 26; i++) {
        if (cnt[i] > 0) {
            if (!f.has(cnt[i])) f.set(cnt[i], '');
            f.set(cnt[i], f.get(cnt[i]) + String.fromCharCode(97 + i));
        }
    }
    let mx = 0, mv = 0, ans = '';
    for (const [v, cs] of f) {
        if (cs.length > mx || (cs.length === mx && v > mv)) {
            mx = cs.length;
            mv = v;
            ans = cs;
        }
    }
    return ans;
}
