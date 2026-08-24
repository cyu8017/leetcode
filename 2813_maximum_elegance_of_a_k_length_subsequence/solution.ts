// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

export function findMaximumElegance(items: number[][], k: number): number {
    items.sort((a, b) => b[0] - a[0]);
    const seen = new Set();
    let total = 0;
    const dup = [];
    for (let i = 0; i < k; i++) {
        total += items[i][0];
        const c = items[i][1];
        if (seen.has(c)) dup.push(items[i][0]);
        else seen.add(c);
    }
    let ans = total + seen.size * seen.size;
    for (let i = k; i < items.length; i++) {
        const c = items[i][1];
        if (seen.has(c) || !dup.length) continue;
        total += items[i][0] - dup.pop();
        seen.add(c);
        ans = Math.max(ans, total + seen.size * seen.size);
    }
    return ans;
}
