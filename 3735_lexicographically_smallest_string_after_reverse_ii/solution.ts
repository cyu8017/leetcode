// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

export function lexSmallest(s: any): any {
    const n = s.length;
    let best = s;
    const reverse = (a, l, r) => {
        for (let i = l, j = r - 1; i < j; i++, j--) {
            const t = a[i]; a[i] = a[j]; a[j] = t;
        }
    };
    for (let i = 1; i <= n; i++) {
        const t = s.split('');
        reverse(t, 0, i);
        const ts = t.join('');
        if (ts < best) best = ts;
    }
    for (let i = 0; i < n; i++) {
        const t = s.split('');
        reverse(t, i, n);
        const ts = t.join('');
        if (ts < best) best = ts;
    }
    return best;
}
