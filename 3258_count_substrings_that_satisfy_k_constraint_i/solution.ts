// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

export function countKConstraintSubstrings(s: any, k: any): any {
    let ans = 0;
    const n = s.length;
    for (let i = 0; i < n; i++) {
        let z = 0, o = 0;
        for (let j = i; j < n; j++) {
            if (s[j] === '0') z++; else o++;
            if (z <= k || o <= k) ans++;
            else break;
        }
    }
    return ans;
}
