// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

export function minimumTime(s: string): number {
    const n = s.length;
    const left = new Array(n).fill(0);
    if (s[0] === '1') left[0] = 1;
    for (let i = 1; i < n; i++) {
        left[i] = left[i - 1];
        if (s[i] === '1') left[i] = Math.min(i + 1, left[i - 1] + 2);
    }
    let ans = left[n - 1], right = 0;
    for (let i = n - 1; i >= 0; i--) {
        if (s[i] === '1') right = Math.min(n - i, right + 2);
        const leftCost = i > 0 ? left[i - 1] : 0;
        ans = Math.min(ans, leftCost + right);
    }
    return ans;
}
