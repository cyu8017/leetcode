// LeetCode 3628 - Maximum Number of Subsequences After One Inserting
// https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/

export function numOfSubsequences(s: any): any {
    const calc = (str, t) => {
        let cnt = 0, a = 0;
        for (const c of str) {
            if (c === t[1]) cnt += a;
            if (c === t[0]) a++;
        }
        return cnt;
    };
    let l = 0, r = 0;
    for (const c of s) if (c === 'T') r++;
    let ans = 0, mx = 0;
    for (const c of s) {
        if (c === 'T') r--;
        if (c === 'C') ans += l * r;
        if (c === 'L') l++;
        mx = Math.max(mx, l * r);
    }
    mx = Math.max(mx, Math.max(calc(s, 'LC'), calc(s, 'CT')));
    return ans + mx;
}
