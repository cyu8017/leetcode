// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

export function smallestNumber(pattern: string): string {
    const n = pattern.length;
    const ans = Array(n + 1);
    for (let i = 0; i <= n; i++) ans[i] = String.fromCharCode(49 + i);
    let i = 0;
    while (i < n) {
        if (pattern[i] === 'I') { i++; continue; }
        let j = i;
        while (j < n && pattern[j] === 'D') j++;
        let l = i, r = j;
        while (l < r) {
            const t = ans[l]; ans[l] = ans[r]; ans[r] = t;
            l++; r--;
        }
        i = j;
    }
    return ans.join('');
}
