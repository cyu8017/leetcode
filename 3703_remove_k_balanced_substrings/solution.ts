// LeetCode 3703 - Remove K-Balanced Substrings
// https://leetcode.com/problems/remove-k-balanced-substrings/

export function removeSubstring(s: any, k: any): any {
    const stk = [];
    for (const c of s) {
        if (stk.length && stk[stk.length - 1][0] === c)
            stk[stk.length - 1][1]++;
        else stk.push([c, 1]);
        if (c === ')' && stk.length > 1) {
            const top = stk[stk.length - 1];
            const prev = stk[stk.length - 2];
            if (top[1] === k && prev[1] >= k) {
                stk.pop();
                prev[1] -= k;
                if (prev[1] === 0) stk.pop();
            }
        }
    }
    let res = '';
    for (const p of stk)
        for (let i = 0; i < p[1]; i++) res += p[0];
    return res;
}
