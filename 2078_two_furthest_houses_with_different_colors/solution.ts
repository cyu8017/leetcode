// LeetCode 2078 - Two Furthest Houses With Different Colors
// https://leetcode.com/problems/two-furthest-houses-with-different-colors/

export function maxDistance(colors: number[]): number {
    const n = colors.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        if (colors[i] !== colors[0]) ans = Math.max(ans, i);
        if (colors[i] !== colors[n - 1]) ans = Math.max(ans, n - 1 - i);
    }
    return ans;
}
