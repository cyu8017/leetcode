// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

export function minimumOperations(num: string): number {
    const n = num.length;
    let ans = n;
    if (num.includes('0')) ans = Math.min(ans, n - 1);
    for (const t of ['00', '25', '50', '75']) {
        let j = n - 1;
        while (j >= 0 && num[j] !== t[1]) j--;
        if (j < 0) continue;
        let i = j - 1;
        while (i >= 0 && num[i] !== t[0]) i--;
        if (i < 0) continue;
        ans = Math.min(ans, n - i - 2);
    }
    return ans;
}
