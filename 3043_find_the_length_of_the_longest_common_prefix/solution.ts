// LeetCode 3043 - Find the Length of the Longest Common Prefix
// https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/

export function longestCommonPrefix(arr1: any, arr2: any): any {
    const s = new Set();
    for (const x0 of arr1) {
        for (let x = x0; x > 0; x = (x / 10) | 0) s.add(x);
    }
    let mx = 0;
    for (const x0 of arr2) {
        for (let x = x0; x > 0; x = (x / 10) | 0) {
            if (s.has(x)) {
                mx = Math.max(mx, x);
                break;
            }
        }
    }
    return mx > 0 ? String(mx).length : 0;
}
