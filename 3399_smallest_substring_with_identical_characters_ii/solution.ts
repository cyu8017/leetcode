// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

export function minLength(s: any, numOps: any): any {
    const n = s.length;
    const ok = (L) => {
        let ops = 0;
        for (let i = 0; i < n; ) {
            let j = i;
            while (j < n && s[j] === s[i]) j++;
            ops += Math.floor((j - i) / (L + 1));
            i = j;
        }
        return ops <= numOps;
    };
    let lo = 1, hi = n;
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
