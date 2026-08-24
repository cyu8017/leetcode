// LeetCode 2014 - Longest Subsequence Repeated K Times
// https://leetcode.com/problems/longest-subsequence-repeated-k-times/

export function longestSubsequenceRepeatedK(s: string, k: number): string {
    const freq = new Array(26).fill(0);
    for (const c of s) freq[c.charCodeAt(0) - 97]++;
    let chars = "";
    for (let c = 25; c >= 0; c--) if (freq[c] >= k) chars += String.fromCharCode(97 + c);
    const isSubseq = (t) => {
        let need = 0, times = 0;
        for (let i = 0; i < s.length; i++) {
            if (s[i] === t[need]) {
                need++;
                if (need === t.length) {
                    times++;
                    if (times === k) return true;
                    need = 0;
                }
            }
        }
        return false;
    };
    let best = "";
    const q = [""];
    while (q.length) {
        const cur = q.shift();
        for (let i = 0; i < chars.length; i++) {
            const nxt = cur + chars[i];
            if (isSubseq(nxt)) {
                if (nxt.length > best.length || (nxt.length === best.length && nxt > best))
                    best = nxt;
                q.push(nxt);
            }
        }
    }
    return best;
}
