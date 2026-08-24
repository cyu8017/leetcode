// LeetCode 2865 - Beautiful Towers I
// https://leetcode.com/problems/beautiful-towers-i/

export function maximumSumOfHeights(heights: number[]): number {
    const n = heights.length;
    let ans = 0;
    for (let peak = 0; peak < n; peak++) {
        let sum = heights[peak];
        let mn = heights[peak];
        for (let i = peak - 1; i >= 0; i--) {
            if (heights[i] < mn) mn = heights[i];
            sum += mn;
        }
        mn = heights[peak];
        for (let i = peak + 1; i < n; i++) {
            if (heights[i] < mn) mn = heights[i];
            sum += mn;
        }
        if (sum > ans) ans = sum;
    }
    return ans;
}
