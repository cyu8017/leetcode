// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

export function lexSmallest(s: any): any {
    let ans = s;
    const n = s.length;
    const reverse = (a, l, r) => {
        for (let i = l, j = r - 1; i < j; i++, j--) {
            const t = a[i]; a[i] = a[j]; a[j] = t;
        }
    };
    for (let k = 1; k <= n; k++) {
        const a1 = s.split('');
        reverse(a1, 0, k);
        const t1 = a1.join('');
        const a2 = s.split('');
        reverse(a2, n - k, n);
        const t2 = a2.join('');
        if (t1 < ans) ans = t1;
        if (t2 < ans) ans = t2;
    }
    return ans;
}
